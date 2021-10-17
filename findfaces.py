import face_recognition
from face_recognition.api import face_locations

image = face_recognition.load_image_file('./img/groups/team1.jpeg')
face_locations = face_recognition.face_locations(image)

#array of coordinates of each face
print(face_locations)

print(f'{len(face_locations)} people detected in this image.')