def persnol_info(phone):
    if phone == '03059601725':
        name = 'Ghulam Mustafa'
        age = 22
        id = 3550403856881
        blood = 'B+V'
        edu = '12th Pass'
        address = 'Lala Town nearby Al-minar Masjad, Fortabbas.'
        print('%s is registered on the person name is %s and CNIC number is %s\nPerson Details:\nHe lives in %s\n%s age is %s and his Blood Group is %s.'%(phone,name,id,address,name,age,blood))

persnol_info('03059601725')
