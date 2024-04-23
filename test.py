import requests

base_url = 'http://localhost:8000/api/student/create-student/'  # API URL manzili

# Talaba ma'lumotlari
student_data = {
    'image': open('photo.jpg', 'rb'),  # Rasmdagi yo'l
    
}
data = {
  "id": 1,
  "school": '13',
  "schoolClass": "10A",
  "telegramId": 1112,
  "image": open('photo.jpg','rb'),
  "fullname": "Sarvar",
  "phone": 8881365141,
  "motto": "Salom qilish",
  "city": "Bukhara",
  "district": "g'ijduvon",
  "level": 0,
  "is_active": False
}
# Talaba yaratish (create_student)
response = requests.post(base_url, data=data, files=student_data)

print(response.json())