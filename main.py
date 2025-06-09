import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':

    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    active_passcards = Passcard.objects.filter(is_active=True)
    all_passcards = Passcard.objects.all()

    print(f'Количество активных пропусков: {active_passcards.count()}')
