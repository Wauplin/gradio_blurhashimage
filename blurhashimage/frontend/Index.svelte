<svelte:options accessors={true} />

<script context="module" lang="ts">
	export { default as BaseStaticImage } from "./shared/ImagePreview.svelte";
	export { default as BaseExample } from "./Example.svelte";
</script>

<script lang="ts">
	import type { Gradio, SelectData } from "@gradio/utils";
	import StaticImage from "./shared/ImagePreview.svelte";

	import { Block } from "@gradio/atoms";
	import { StatusTracker } from "@gradio/statustracker";
	import type { BlurhashFileData } from "./shared/data";
	import type { LoadingStatus } from "@gradio/statustracker";

	export let elem_id = "";
	export let elem_classes: string[] = [];
	export let visible = true;
	export let value: null | BlurhashFileData = null;
	export let label: string;
	export let show_label: boolean;
	export let show_download_button: boolean;
	export let root: string;

	export let height: number | undefined;
	export let width: number | undefined;

	export let container = true;
	export let scale: number | null = null;
	export let min_width: number | undefined = undefined;
	export let loading_status: LoadingStatus;
	export let show_share_button = false;

	export let gradio: Gradio<{
		change: never;
		error: string;
		edit: never;
		stream: never;
		drag: never;
		upload: never;
		clear: never;
		select: SelectData;
		share: ShareData;
	}>;

	$: console.log(value);
	$: value?.image?.url && gradio.dispatch("change");
	let dragging: boolean;

	$: value = !value ? null : value;
</script>

<Block
	{visible}
	variant={"solid"}
	border_mode={dragging ? "focus" : "base"}
	padding={false}
	{elem_id}
	{elem_classes}
	height={height || undefined}
	{width}
	allow_overflow={false}
	{container}
	{scale}
	{min_width}
>
	<StatusTracker
		autoscroll={gradio.autoscroll}
		i18n={gradio.i18n}
		{...loading_status}
	/>
	<StaticImage
		on:select={({ detail }) => gradio.dispatch("select", detail)}
		on:share={({ detail }) => gradio.dispatch("share", detail)}
		on:error={({ detail }) => gradio.dispatch("error", detail)}
		{root}
		{value}
		{label}
		{show_label}
		{show_download_button}
		{show_share_button}
		i18n={gradio.i18n}
	/>
</Block>
