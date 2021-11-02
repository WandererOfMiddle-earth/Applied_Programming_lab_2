from json import load as json_load
from re import match as re_match
from tqdm import tqdm
import argparse


class сharacteristics:
    '''
    Объект класса сharacteristics содержит характеристики некоторого
    научного сотрудника.
    
    Attributes
    -----------------------------------------------------------------
        _telephone: str
            Номер телефона – строка, объектное свойство класса
            сharacteristics.
        _weight: str
            Вес – строка, объектное свойство класса сharacteristics.
        _snils: str
            Номер СНИЛСа – строка, объектное свойство класса
            сharacteristics.
        _passport_series: str
            Серия паспорта – строка, объектное свойство класса
            сharacteristics.
        _university: str
            Название университета – строка, объектное свойство класса
            сharacteristics.
        _age: str
            Возраст – строка, объектное свойство класса
            сharacteristics.
        _political_views: str
            Политические взгляды – строка, объектное свойство класса
            сharacteristics.
        _worldview: str
            Мировоззрение – строка, объектное свойство класса
            сharacteristics.
        _address: str
            Адрес проживания – строка, объектное свойство класса
            сharacteristics.
    '''    
    
    def __init__(self, telephone: str or int, 
                 weight: str or int, 
                 snils: str or int, 
                 passport_series: str or int, 
                 university: str, 
                 age: str or int, 
                 political_views: str, 
                 worldview: str, 
                 address: str) -> None:
        '''
        Инициализирует экземпляр класса сharacteristics.
        
        Parameters
        -------------------------------------------
            telephone: str or int
                Строка/целое число; номер телефона.
            weight: str or int
                Строка/целое число; вес.
            snils: str or int
                Строка/целое число; СНИЛС.
            passport_series: str or int
                Строка/целое число; серию паспорта.
            university: str
                Строка; название университета.
            age: str or int
                Строка/целое число; возраст.
            political_views: str
                Строка; политические взгляды.
            worldview: str
                Строка; мировоззрение.
            address: str
                Строка; адрес проживания.
        '''
        self._telephone = str(telephone)
        self._weight = str(weight)
        self._snils = str(snils)
        self._passport_series = str(passport_series)
        self._university = university
        self._age = str(age)
        self._political_views = political_views
        self._worldview = worldview
        self._address = address
    
    @property
    def all_str(self) -> str:
        '''
        Возвращает строку со всеми объектными свойствами класса
        сharacteristics.
        
        Returns
        ---------------------------------------------------------
            str:
                Строка вида:
                '_telephone; _weight; ...; _worldview; _address'.
        '''
        return (self._telephone + '; ' + 
                self._weight + '; ' + 
                self._snils + '; ' + 
                self._passport_series + '; ' + 
                self._university + '; ' + 
                self._age + '; ' + 
                self._political_views + '; ' + 
                self._worldview + '; ' + self._address)
    
    @property
    def all_list(self) -> list:
        '''
        Возвращает массив со всеми объектными свойствами класса
        сharacteristics.
        
        Returns
        -----------------------------------------------------------
            list:
                Массив вида:
                [ _telephone, _weight, ..., _worldview, _address ].
        '''
        return [ self._telephone, self._weight, self._snils, 
                 self._passport_series, self._university, self._age, 
                 self._political_views, self._worldview, self._address ]
    
    @property
    def telephone(self) -> str:
        '''
        Возвращает _telephone – объектное свойство класса
        сharacteristics.
        
        Returns
        --------------------------
            str:
                Строка _telephone.
        '''
        return self._telephone
    
    @property
    def weight(self) -> str:
        '''
        Возвращает _weight – объектное свойство класса сharacteristics.
        
        Returns
        -----------------------
            str:
                Строка _weight.
        '''
        return self._weight
    
    @property
    def snils(self) -> str:
        '''
        Возвращает _snils – объектное свойство класса сharacteristics.
        
        Returns
        ----------------------
            str:
                Строка _snils.
        '''
        return self._snils
    
    @property
    def passport_series(self) -> str:
        '''
        Возвращает _passport_series – объектное свойство класса
        сharacteristics.
        
        Returns
        --------------------------------
            str:
                Строка _passport_series.
        '''
        return self._passport_series
    
    @property
    def university(self) -> str:
        '''
        Возвращает _university – объектное свойство класса
        сharacteristics.
        
        Returns
        ---------------------------
            str:
                Строка _university.
        '''
        return self._university
    
    @property
    def age(self) -> str:
        '''
        Возвращает _age – объектное свойство класса сharacteristics.
        
        Returns
        --------------------
            str:
                Строка _age.
        '''
        return self._age
    
    @property
    def political_views(self) -> str:
        '''
        Возвращает _political_views – объектное свойство класса
        сharacteristics.
        
        Returns
        --------------------------------
            str:
                Строка _political_views.
        '''
        return self._political_views
    
    @property
    def worldview(self) -> str:
        '''
        Возвращает _worldview – объектное свойство класса
        сharacteristics.
        
        Returns
        --------------------------
            str:
                Строка _worldview.
        '''
        return self._worldview
    
    @property
    def address(self) -> str:
        '''
        Возвращает _address – объектное свойство класса
        сharacteristics.
        
        Returns
        ------------------------
            str:
                Строка _address.
        '''
        return self._address


class validator:
    '''
    Объект класса содержит объект класса characteristics.
    
    Attributes
    -------------------------------------------
        _obj: characteristics
            Объект класса сharacteristics.
    '''
    
    def __init__(self, obj: сharacteristics) -> None:
        '''
        Инициализирует экземпляр класса validator.
        
        Parameters
        --------------------------------------
            obj: сharacteristics
                Объект класса сharacteristics.
        '''
        self._obj = obj

    @property
    def telephone_correctness(self) -> bool:
        '''
        Выполняет проверку корректности записи _telephone – объектного
        свойства объекта класса сharacteristics.
        
        Если строка _telephone соответствует типу '+7-(xxx)-xxx-xx-xx',
        где x – число от 0 до 9, будет возвращено True, иначе – False.
        
        Returns
        ---------------------------------------------------
            bool:
                Булевый результат проверки на корректность.
        ''' 
        pattern = r'^\+7-\([0-9]{3}\)-[0-9]{3}-[0-9]{2}-[0-9]{2}$'
        if re_match(pattern, self._obj.telephone):
            return True
        return False
    
    @property
    def weight_correctness(self) -> bool:
        '''
        Выполняет проверку корректности записи _weight – объектного
        свойства объекта класса сharacteristics.
        
        Если значение _weight – целое число, которое находится в
        отрезке [35, 120], будет возвращено True, иначе – False.
            
        Returns
        ---------------------------------------------------
            bool:
                Булевый результат проверки на корректность.
        '''
        pattern = r'^[0-9]*$'
        if re_match(pattern, self._obj.weight) and 35 <= int(self._obj.weight) <= 120:
            return True
        return False

    @property
    def snils_correctness(self) -> bool:
        '''
        Выполняет проверку корректности записи _snils – объектного
        свойства объекта класса сharacteristics.
        
        Если строка _snils соответствует типу 'xxxxxxxxxxx', где x –
        число от 0 до 9, будет возвращено True, иначе – False.
            
        Returns
        ---------------------------------------------------
            bool:
                Булевый результат проверки на корректность.
        '''
        pattern = r'^[0-9]{11}$'
        if re_match(pattern, self._obj.snils):
            return True
        return False
    
    @property
    def passport_series_correctness(self) -> bool:
        '''
        Выполняет проверку корректности записи _passport_series –
        объектного свойства объекта класса сharacteristics.
        
        Если строка passport_series соответствует типу 'xx xx', где x –
        число от 0 до 9, будет возвращено True, иначе – False.
            
        Returns
        ---------------------------------------------------
            bool:
                Булевый результат проверки на корректность.
        '''
        pattern = r'^[0-9]{2} [0-9]{2}$'
        if re_match(pattern, self._obj.passport_series):
            return True
        return False
    
    @property
    def university_correctness(self) -> bool:
        '''
        Выполняет проверку корректности записи _university – объектного
        свойства объекта класса сharacteristics.
        
        Если значение _university допустимо, будет возвращено True,
        иначе – False.
        Допустимых значених _university много, поэтому обозначим только
        недопустимые:
        - 'Шармбатон'
        - 'Бан Ард'
        - 'Кирин-Тор'
        - 'Дурмстранг'
        - 'Гвейсон Хайль'
        - 'Аретуза'
        - 'Каражан'
        - 'Хогвартс'
        
        Returns
        ---------------------------------------------------
            bool:
                Булевый результат проверки на корректность.
        '''
        pattern = r'^Шармбатон|Бан Ард|Кирин-Тор|Дурмстранг|Гвейсон Хайль|Аретуза|Каражан|Хогвартс$'
        if re_match(pattern, self._obj.university):
            return False
        return True
    
    @property
    def age_correctness(self) -> bool:
        '''
        Выполняет проверку корректности записи _age –
        объектного свойства объекта класса сharacteristics.
        
        Если значение _age – целое число, которое находится в
        отрезке [16, 80], будет возвращено True, иначе – False.
            
        Returns
        ---------------------------------------------------
            bool:
                Булевый результат проверки на корректность.
        '''
        pattern = r'^[0-9]*$'
        if re_match(pattern, self._obj.age) and 16 <= int(self._obj.age) <= 80:
            return True
        return False
    
    @property
    def political_views_correctness(self) -> bool:
        '''
        Выполняет проверку корректности записи _political_views –
        объектного свойства объекта класса сharacteristics.
        
        Если значение _political_views допустимо, будет возвращено True,
        иначе – False.
        Допустимые значения _political_views:
        - 'Анархистские'
        - 'Либеральные'
        - 'Либертарианские'
        - 'Коммунистические'
        - 'Социалистические'
        - 'Умеренные'
        - 'Индифферентные'
        - 'Консервативные'
            
        Returns
        ---------------------------------------------------
            bool:
                Булевый результат проверки на корректность.
        '''
        pattern = r'^Анархистские|Либеральные|Либертарианские|Коммунистические|Социалистические|Умеренные|Индифферентные|Консервативные$'
        if re_match(pattern, self._obj.political_views):
            return True
        return False

    @property
    def worldview_correctness(self) -> bool:
        '''
        Выполняет проверку корректности записи _worldview – объектного
        свойства объекта класса сharacteristics.
        
        Если значение _worldview допустимо, будет возвращено True,
        иначе – False.
        Допустимые значения _worldview:
        - 'Секулярный гуманизм'
        - 'Атеизм'
        - 'Иудаизм'
        - 'Пантеизм'
        - 'Деизм'
        - 'Конфуцианство'
        - 'Буддизм'
        - 'Агностицизм'
        - 'Католицизм'
        
        Returns
        ---------------------------------------------------
            bool:
                Булевый результат проверки на корректность.
        '''
        pattern = r'^Секулярный гуманизм|Атеизм|Иудаизм|Пантеизм|Деизм|Конфуцианство|Буддизм|Агностицизм|Католицизм$'
        if re_match(pattern, self._obj.worldview):
            return True
        return False
    
    @property
    def address_correctness(self) -> bool:
        '''
        Выполняет проверку корректности записи _address – объектного
        свойства объекта класса сharacteristics.
        
        Если строка _address соответствует типу 'a b cd', где
        a – 'Аллея' ИЛИ 'ул.',
        b – название, которое состоит из одного или нескольких слов и
            может начинаться числом,
        c – 'd-я ' ИЛИ 'dБУКВА ' ИЛИ 'd км ' ИЛИ '',
        d – целое число,
        будет возвращено True, иначе – False.
        
        Returns
        ---------------------------------------------------
            bool:
                Булевый результат проверки на корректность.
        '''
        pattern = r'^(?:Аллея |ул\. ){1}[0-9]*\D+(?:[1-9]*-я |[0-9]+[а-я] |[0-9]* км )?[0-9]*$'
        if re_match(pattern, self._obj.address):
            return True
        return False       


parser = argparse.ArgumentParser(description = '')
parser.add_argument('-i', '--inputway', type = str, default = '', 
                    help = 'Строка, содержащая путь к папке, в которой \
                    находится файл с данными, которые нужно считать. \
                    По умолчанию строка пуста, т.е. подразумевается, \
                    что файл находится в той же папке, что и \
                    исполняемая программа.')
parser.add_argument('inputfile', type = str, 
                    help = 'Файл, который требуется считать')
parser.add_argument('-o', '--outputway', type = str, default = '', 
                    help = 'Строка, содержащая путь к папке, в которой \
                    находится файл, в который нужно записать \
                    обработанные данные. По умолчанию строка пуста, \
                    т.е. подразумевается, что файл находится в той же \
                    папке, что и исполняемая программа.')
parser.add_argument('outputfile', type = str, 
                    help = 'Файл, который требуется записать \
                    обработанные данные')

flag = True
while (flag):
    args = parser.parse_args()
    try:
        file = open(args.inputway + '\\' + args.inputfile, encoding = 'windows-1251')
    except OSError:
        print('Invalid way to file or file opening error...')
    else:
        flag = False
elements = json_load(file)
file.close()

k = 0
c_list = []
progressbar = tqdm(elements, desc = 'Putting data into a class')
for element in progressbar:
    c = сharacteristics(element['telephone'], 
                         str(element['weight']), 
                         str(element['snils']), 
                         str(element['passport_series']), 
                         element['university'], 
                         str(element['age']), 
                         element['political_views'], 
                         element['worldview'], 
                         element['address'])
    c_list.append(c)
    k += 1

all_correct = []
invalid_telephone = []
invalid_weight = []
invalid_snils = []
invalid_passport_series = []
invalid_university = []
invalid_age = []
invalid_political_views = []
invalid_worldview = []
invalid_address = []

progressbar = tqdm(c_list, desc = 'Validation')
for c in progressbar:
    v = validator(c)
    if not v.telephone_correctness:
        invalid_telephone.append(c)
    elif not v.weight_correctness:
        invalid_weight.append(c)
    elif not v.snils_correctness:
        invalid_snils.append(c)
    elif not v.passport_series_correctness:
        invalid_passport_series.append(c)
    elif not v.university_correctness:    
        invalid_university.append(c)
    elif not v.age_correctness:
        invalid_age.append(c)
    elif not v.political_views_correctness:
        invalid_political_views.append(c)
    elif not v.worldview_correctness:
        invalid_worldview.append(c)
    elif not v. address_correctness:
        invalid_address.append(c)
    else:
        all_correct.append(c)

output = open(args.outputway + '\\' + args.outputfile, 'w')
for c in all_correct:
    output.write(c.all_str + '\n')
output.close()

print('\nНемного статистики:')
print(f'Количество записей в файле: {k}')
print(f'Количество валидных записей: {len(all_correct)}')
print('Количество записей с невалидным номером телефона: %d ; \
составляют %.3f%% от общего числа записей' 
      % (len(invalid_telephone), 
         len(invalid_telephone) / k * 100))
print('Количество записей с невалидным весом: %d ; \
составляют %.3f%% от общего числа записей' 
      % (len(invalid_weight), 
         len(invalid_weight) / k * 100))
print('Количество записей с невалидным СНИЛСом: %d ; \
составляют %.3f%% от общего числа записей' 
      % (len(invalid_snils), 
         len(invalid_snils) / k * 100))
print('Количество записей с невалидной серией паспорта: %d ; \
составляют %.3f%% от общего числа записей' 
      % (len(invalid_passport_series), 
         len(invalid_passport_series) / k * 100))
print('Количество записей с невалидным названием университета: %d ; \
составляют %.3f%% от общего числа записей' 
      % (len(invalid_university), 
         len(invalid_university) / k * 100))
print('Количество записей с невалидным возрастом: %d ; \
составляют %.3f%% от общего числа записей' 
      % (len(invalid_age), 
         len(invalid_age) / k * 100))
print('Количество записей с невалидными политическиими взглядами: %d ; \
составляют %.3f%% от общего числа записей' 
      % (len(invalid_political_views), 
         len(invalid_political_views) / k * 100))
print('Количество записей с невалидным мировоззрением: %d ; \
составляют %.3f%% от общего числа записей' 
      % (len(invalid_worldview), 
         len(invalid_worldview) / k * 100))
print('Количество записей с невалидным адресом проживания: %d ; \
составляют %.3f%% от общего числа записей' 
      % (len(invalid_address), 
         len(invalid_address) / k * 100))