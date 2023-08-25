from texere import edges

edged_image=edges.mark(input_image_path="image_path",threshold=70)

edged_image.save("image_path")