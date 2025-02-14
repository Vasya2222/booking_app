from django.shortcuts import render
from django.http import HttpResponse

from booking_app.models import Room


def index(request):
    return render(request, 'booking_app/index.html')


def about(request):
    return HttpResponse('О нас')


def rooms(request):
    # Получаем все комнаты из базы данных
    rooms_db = Room.objects.all()

    rooms = [
        {
            'id': room.id,  # Идентификатор комнаты
            'number': room.number,
            'image_url': room.image,  # Путь к изображению комнаты

            'type': room.category,  # Получаем отображаемое имя категории
            'price': room.price,  # Цена
            'available': room.available  # Доступность

        }
        for room in rooms_db
    ]
    return render(request, 'booking_app/rooms.html', {'rooms': rooms})
