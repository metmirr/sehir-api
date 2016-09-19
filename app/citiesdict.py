#-*- coding: utf-8 -*-
'''
    Şehirlerin listesini tutan sözlük
'''
cities = [
		{
            'name': 'Adana',
            'city_code': 1
        },
        {
            'name': 'Adiyaman',
            'city_code': 2
        },
        {
            'name': 'Afyonkarahisar',
            'city_code': 3
        },
        {
            'name': 'Agri',
            'city_code': 4
        },
        {
            'name': 'Amasya',
            'city_code': 5
        },
        {
            'name': 'Ankara',
            'city_code': 6
        },
        {
            'name': 'Antalya',
            'city_code': 7
        },
        {
            'name': 'Artvin',
            'city_code': 8
        },
        {
            'name': 'Aydin',
            'city_code': 9
        },
        {
            'name': 'Balikesir',
            'city_code': 10
        },
        {
            'name': 'Bilecik',
            'city_code': 11
        },
        {
            'name': 'Bingol',
            'city_code': 12
        },
        {
            'name': 'Bitlis',
            'city_code': 13
        },
        {
            'name': 'Bolu',
            'city_code': 14
        },
        {
            'name': 'Burdur',
            'city_code': 15
        },
        {
            'name': 'Bursa',
            'city_code': 16
        },
        {
            'name': 'Canakkale',
            'city_code': 17
        },
        {
            'name': 'Cankiri',
            'city_code': 18
        },
        {
            'name': 'Corum',
            'city_code': 19
        },
        {
            'name': 'Denizli',
            'city_code': 20
        },
        {
            'name': 'Diyarbakir',
            'city_code': 21
        },
        {
            'name': 'Edirne',
            'city_code': 22
        },
        {
            'name': 'Elazig',
            'city_code': 23
        },
        {
            'name': 'Erzincan',
            'city_code': 24
        },
        {
            'name': 'Erzurum',
            'city_code': 25
        },
        {
            'name': 'Eskisehir',
            'city_code': 26
        },
        {
            'name': 'Gaziantep',
            'city_code': 27
        },
        {
            'name': 'Giresun',
            'city_code': 28
        },
        {
            'name': 'Gumushane',
            'city_code': 29
        },
        {
            'name': 'Hakkari',
            'city_code': 30
        },
        {
            'name': 'Hatay',
            'city_code': 31
        },
        {
            'name': 'Isparta',
            'city_code': 32
        },
        {
            'name': 'Mersin',
            'city_code': 33
        },
        {
            'name': 'Istanbul',
            'city_code': 34
        },
        {
            'name': 'Izmir',
            'city_code': 35
        },
        {
            'name': 'Kars',
            'city_code': 36
        },
        {
            'name': 'Kastamonu',
            'city_code': 37
        },
        {
            'name': 'Kayseri',
            'city_code': 38
        },
        {
            'name': 'Kirklareli',
            'city_code': 39
        },
        {
            'name': 'Kirsehir',
            'city_code': 40
        },
        {
            'name': 'Kocaeli',
            'city_code': 41
        },
        {
            'name': 'Konya',
            'city_code': 42
        },
        {
            'name': 'Kutahya',
            'city_code': 43
        },
        {
            'name': 'Malatya',
            'city_code': 44
        },
        {
            'name': 'Manisa',
            'city_code': 45
        },
        {
            'name': 'Kahramanmaras',
            'city_code': 46
        },
        {
            'name': 'Mardin',
            'city_code': 47
        },
        {
            'name': 'Mugla',
            'city_code': 48
        },
        {
            'name': 'Mus',
            'city_code': 49
        },
        {
            'name': 'Nevsehir',
            'city_code': 50
        },
        {
            'name': 'Nigde',
            'city_code': 51
        },
        {
            'name': 'Ordu',
            'city_code': 52
        },
        {
            'name': 'Rize',
            'city_code': 53
        },
        {
            'name': 'Sakarya',
            'city_code': 54
        },
        {
            'name': 'Samsun',
            'city_code': 55
        },
        {
            'name': 'Siirt',
            'city_code': 56
        },
        {
            'name': 'Sinop',
            'city_code': 57
        },
        {
            'name': 'Sivas',
            'city_code': 58
        },
        {
            'name': 'Tekirdag',
            'city_code': 59
        },
        {
            'name': 'Tokat',
            'city_code': 60
        },
        {
            'name': 'Trabzon',
            'city_code': 61
        },
        {
            'name': 'Tunceli',
            'city_code': 62
        },
        {
            'name': 'Sanliurfa',
            'city_code': 63
        },
        {
            'name': 'Usak',
            'city_code': 64
        },
        {
            'name': 'Van',
            'city_code': 65
        },
        {
            'name': 'Yozgat',
            'city_code': 66
        },
        {
            'name': 'Zonguldak',
            'city_code': 67
        },
        {
            'name': 'Aksaray',
            'city_code': 68
        },
        {
            'name': 'Bayburt',
            'city_code': 69
        },
        {
            'name': 'Karaman',
            'city_code': 70
        },
        {
            'name': 'Kirikkle',
            'city_code': 71
        },
        {
            'name': 'Batman',
            'city_code': 72
        },
        {
            'name': 'Sirnak',
            'city_code': 73
        },
        {
            'name': 'Bartin',
            'city_code': 74
        },
        {
            'name': 'Ardahan',
            'city_code': 75
        },
        {
            'name': 'Igdir',
            'city_code': 76
        },
        {
            'name': 'Yalova',
            'city_code': 77
        },
        {
            'name': 'Karabuk',
            'city_code': 78
        },
        {
            'name': 'Kilis',
            'city_code': 79
        },
        {
            'name': 'Osmaniye',
            'city_code': 80
        },
        {
            'name': 'Duzce',
            'city_code': 81
        }
]
