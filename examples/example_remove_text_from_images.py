from texere import purge
import cv2

purged_image,mask=purge.txt(input_image_path="image_path",pixels=5,threshold=0)

#example here Im using cv2 to impaint the purged_image wsing mask

radius = 2  # Radius of the inpainting neighborhood
inpainting_result = cv2.inpaint(purged_image,mask, radius, cv2.INPAINT_TELEA)  # Use INPAINT_TELEA or INPAINT_NS
# Save the inpainting result
cv2.imwrite("inpainting_result.jpg", inpainting_result)