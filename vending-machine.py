sum = 0
mahsulotlar = {'Cola': 5000, 'Tuc': 3000, 'Oreo': 5000, '18+': 8000,
               'Orbit': 5000, 'Ice Tea': 4000, 'Kit kat': 6000, 'Lays': 5000, 'Flesh': 6000, 'Alpen Gold': 10_000, }
miqdor = {'Cola': 3, 'Tuc': 5, 'Oreo': 12, '18+': 4,
          'Orbit': 1, 'Ice Tea': 8, 'Kit kat': 5, 'Lays': 4, 'Flesh': 8, 'Alpen Gold': 1, }
raqam = {1: 'Cola', 2: 'Tuc', 3: 'Oreo', 4: '18+',
         5: 'Orbit', 6: 'Ice Tea', 7: 'Kit kat', 8: 'Lays', 9: 'Flesh', 10: 'Alpen Gold', }


def pul():  
    global sum
    try:
        curry = [1000, 2000, 5000, 10000]
        print('\nMablag\' kiritish')
        balans = input(
            "Pul kiriting va chiqmoqchi bo'lsangiz 'exit' deb yozing ")
        if balans == 'exit':
            return sum
        elif int(balans) in curry:
            sum += int(balans)
            print(f"\nBalans {sum} pul")
            return pul()
        else:
            print('\nBunday kupyura mavjud emas! Iltimos boshqattan urinib ko\'ring')
        print(pul())
        return ''
    except:
        return pul()




def mahsulotlar_royxati():
    try:
        global sum
        for key, qiymat in enumerate(mahsulotlar, 1):
            if miqdor[qiymat] > 0:
                print(
                    f"{key}.{qiymat}-{mahsulotlar[qiymat]} sum {miqdor[qiymat]} dona ")
            else:
                print("bunday mahsulot mavjud emas, yana urinib ko'ring: ")
                # return ''
        savol = input(
            "Maxsulotlar raqamini tanlang, (dasturni toxtatish uchun 'exit' deb yozing): ")
        if savol == 'exit':
            return ''
        elif int(savol) in raqam:
            if mahsulotlar[raqam[int(savol)]] <= sum:
                if miqdor[raqam[int(savol)]] > 0:
                    print(f"\n{raqam[int(savol)]} tanlandi")
                    miqdor[raqam[int(savol)]] = miqdor[raqam[int(savol)]] - 1
                    sum = sum - mahsulotlar[raqam[int(savol)]]
                    return ''
    except:
        print(mahsulotlar_royxati())
        return ''


def pul_yetadigan_mahsulotlar_royhati():
    try:
        global sum
        for key, qiymat in enumerate(mahsulotlar, 1):
            if sum >= mahsulotlar[qiymat]:
                if miqdor[qiymat] > 0:
                    print(
                        f"{key}.{qiymat}-{mahsulotlar[qiymat]} sum {miqdor[qiymat]} dona ")
        savol = input(
            "Maxsulotlar raqamini tanlang, (dasturni toxtatish uchun 'exit' deb yozing): ")
        if savol == 'exit':
            return ''
        else:
            if sum >= mahsulotlar[raqam[int(savol)]]:
                print(f"\n{raqam[int(savol)]} tanlandi")
                miqdor[raqam[int(savol)]] = miqdor[raqam[int(savol)]] - 1
                sum = sum - mahsulotlar[raqam[int(savol)]]

                return ''

    except:
        print(pul_yetadigan_mahsulotlar_royhati())
        return ''


def qaytim():
    return f"{sum} sum"


def auth():
    try:
        while True:
            sovol = input("""Quydagi buyruqlardan birini tanlang:
            1.pul kiritish
            2.mahsulotlar ro'yxati
            3.pul yetadigan mahsulotlar
            4.qaytim """)
            if sovol == '1':
                print(pul())
            elif sovol == '2':
                print(mahsulotlar_royxati())
            elif sovol == '3':
                print(pul_yetadigan_mahsulotlar_royhati())
            elif sovol == '4':
                print(qaytim())
                break
    
        return ''
    except:
        print("bunday buyruq mavjud emas! Boshqatdan urinib ko'ring ")
        print(auth())
        return ''


print(auth())
