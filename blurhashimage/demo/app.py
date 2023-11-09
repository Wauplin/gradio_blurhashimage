
import gradio as gr
from gradio_blurhashimage import BlurhashImage


example = BlurhashImage().example_inputs()

demo = gr.Interface(
    lambda x:x,
    BlurhashImage(),  # interactive version of your component
    BlurhashImage(),  # static version of your component
    # examples=[[example]],  # uncomment this line to view the "example version" of your component
)


demo.launch()
