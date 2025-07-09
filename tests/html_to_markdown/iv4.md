[![intervolga.ru](/assets/logo/logo.svg)](/)

[+7 495 648 57 90](tel:+74956485790)

* [Разработка на Битрикс](/dev/)
* [Битрикс24](/bitrix24/)
* [1С](/1c/)
* [Интернет-маркетинг](/adv/)
* [Вакансии](/vacancy/)
* [Импортозамещение](/import/)
* [Отрасли](/industries/)

* [Кто мы](/web-integration/)
* [Крупные проекты](/cases/)
* [Портфолио](/portfolio/)
* [Блог](/blog/)
* [Контакты](/contacts/)

![](https://www.intervolga.ru/upload/iblock/3c5/n6cw9w6h1fh8fpap4zwd3e9r0lnzmfvs.png.webp?w=1920)  

1. [Главная](/ "Главная")
2. -
3. [Блог](/blog/ "Блог")
4. -
5. [Веб-Проекты](/blog/projects/ "Веб-Проекты")
6. -
7. [Стандартные и пользовательские свойства в Битриксе](/blog/projects/standartnye-i-polzovatelskie-svoystva-v-bitrikse/ "Стандартные и пользовательские свойства в Битриксе")

# Стандартные и пользовательские свойства в Битриксе

[![](/upload/resize_cache/iblock/a51/60_60_2/a51c9827a2ea7c33b0dfcbde361fc694.png.webp)	  	  	Анатолий Ерофеев](/people/anatoliy_e/) [![](/upload/resize_cache/iblock/de4/60_60_2/de438d59dfefdee82d038a145411208c.png.webp)	  	  	Виктор С.](/people/viktor_s/)

[Подписаться](/subscribe/)

* [Справочник свойств в Битрикс](#section0)
* [Заказы интернет-магазина](#section1)  
  + [Как создать новое свойство](#section2)
  + [Доступные типы](#section3)
* [Интеграция с 1С](#section4)  
  + [Как добавить реквизит](#section5)
  + [Доступные типы](#section6)
* [Элементы инфоблоков](#section7)  
  + [Как создать новое свойство](#section8)
  + [Доступные типы](#section9)
* [Товары в корзине и заказе](#section10)  
  + [Как создать новое свойство](#section11)
  + [Типы свойств](#section12)
* [Компоненты](#section13)  
  + [Как добавить параметр](#section14)
  + [Доступные типы параметров](#section15)
* [Умный фильтр](#section16)  
  + [Как добавить новое свойство](#section17)
  + [Доступные типы](#section18)
* [Страницы и разделы сайта](#section19)  
  + [Как создать новое свойство](#section20)
  + [Типы свойств](#section21)
* [Пункты меню](#section22)  
  + [Как добавить и изменить параметр](#section23)
  + [Доступные типы](#section24)
* [Универсальное решение — пользовательские поля (UF)](#section25)  
  + [Как создать новое свойство](#section26)
  + [Доступные типы](#section27)
* [Внешние сервисы местоположений](#section28)  
  + [Как создать новое свойство](#section29)
  + [Доступные типы](#section30)
* [Заключение](#section31)  
  + [Делимся с самыми любознательными читателями сводной таблицей](#section32)

*Есть они почти везде:*  
*И в публичке и в ядре,*  
*На странице и в товаре,*  
*Даже в склады натыкали*

*О свойствах Битрикса*

В [1С-Битрикс: Управление сайтом](https://www.intervolga.ru/dev/) (как и в [Битрикс24](https://www.intervolga.ru/bitrix24/) ) десятки, если не сотни настраиваемых типов данных (или сущностей): инфоблоки, пользователи, заказы, склады, форумы, блоги и т.д. Структура большинства сущностей расширяема за счет служебной сущности «Свойства».  

В этой статье мы собрали воедино всю информацию о свойствах в Битриксе. Где их создавать в панели управления, как ими управлять через API, какими событиями можно изменить их поведение и как создавать свои собственные типы свойств.  

## Справочник свойств в Битрикс

|  |  |  |
| --- | --- | --- |
| Сущность | Расположение страницы | Что является свойством |
| Заказы интернет-магазина | Рабочий стол > Магазин > Настройки > Свойства заказа > Список свойств | Свойства заказа |
| Элементы инфоблока | Рабочий стол > Контент > Инфоблоки > Типы инфоблоков > [Название инфоблока] > Свойства | Свойства элементов инфоблока |
| Товары каталога | Рабочий стол > Контент > Инфоблоки > Типы инфоблоков > [Название инфоблока] > Свойства | Свойства элементов инфоблока |
| Товары в корзине |  | Свойства товара, добавленного в корзину |
| Товары в заказе |  | Свойства товара, добавленного в корзину |
| Параметры компонентов |  | Файл .parameters.php |
| Параметры шаблонов компонентов |  | Файл .parameters.php |
| Свойства умного фильтра | Рабочий стол > Магазин > Каталоги товаров > [Название инфоблока] > Настройки каталога > Свойства элементов | Свойства элементов инфоблока |
| Страницы и разделы сайта | Рабочий стол > Настройки > Настройки продукта > Настройки модулей > Управление структурой | [Свойства](/upload/medialibrary/3b7/3b7a9ae5bf1e10f38f2b7dda59f48b62.jpg "a5cb41798b.jpg") |
| Пункты меню |  | [Параметры](/upload/medialibrary/817/817f9ec588a20e6ac1c2e38500140cd1.png "c01d7f6d1a.png") |
| Интеграция с 1С | Рабочий стол > Магазин > Настройки > Интеграция с 1С > Профили обмена | [Реквизиты](/upload/medialibrary/ab0/ab042478736ed9bdd365b18202d094a9.jpg "5d439bc124.jpg") |
| Внешние сервисы местоположений | Рабочий стол > Магазин > Настройки > Местоположения > Внешние сервисы | Внешние сервисы |
| Разделы инфоблоков |  | UF |
| HL-блоки | Рабочий стол > Контент > Highload-блоки > [Название HL-блока] > Добавление/редактирование записи | UF |
| Пользователи | Рабочий стол > Настройки > Пользователи > Список пользователей > [Пользователь] > Доп. поля | UF |
| Группы пользователей |  | Нет |
| Склады | Рабочий стол > Магазин > Складской учет > Склады > Добавление/редактирование записи | UF |
| Компании | Рабочий стол > Магазин > Настройки > Компании > Добавление/редактирование компании > Пользовательские поля | UF |
| Обращения в ТП | Рабочий стол > Сервисы > Техподдержка > Обращения > Добавление/редактирование обращения | UF |
| Блоги | Рабочий стол > Сервисы > Блоги > Блоги > Добавление/редактирование блога > Доп. поля | UF |
| Обучение  Курсы  Уроки  Вопрос | Рабочий стол > Сервисы > Обучение > Курсы > Добавление/редактирование > Доп. поля | UF |
| Учебные группы | Рабочий стол > Сервисы > Обучение > Учебные группы > Учебные группы > Добавление/редактирование > Доп. поля | UF |

Рассмотрим для каждой сущности свойства поподробнее: как можно ими управлять, как создать кастомный тип свойства, какие события связаны с изменением свойств и какие возможности оставили нам разработчики [Битрикс](/dev/) .  

## Заказы интернет-магазина

![Карточка заказа в интернет-магазине](/upload/medialibrary/0c6/0c6bc79dc1ef4ed6849308036ae843811.png.webp)  

### Как создать новое свойство

Свойства заказов располагаются по пути: Рабочий стол > Магазин > Настройки > Свойства заказов > Список свойств  
![Правка свойств](/upload/medialibrary/103/103ebaa51f4bed35126eafd0218e742d.png.webp)  

### Доступные типы

В системе «из коробки» есть типы:  

* Строка (STRING);
* Число (NUMBER);
* Да/Нет (Y/N);
* Перечисление (ENUM);
* Файл (FILE);
* Дата (DATE);
* Местоположение (LOCATION).

![Перечисление доступных типов в Битрикс](/upload/medialibrary/136/136f3429a319d52ac7b78f53447c0471.png.webp)  

#### Как добавить свой тип

Типы свойств заказа расширяемы. О том, как создавать кастомные типы свойства заказа рассказывается в курсе [Разработчик Bitrix Framework](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=7350) .  

#### API для работы со значениями

Рассмотрим на примере использование API ядра D7 для работы со значениями свойств заказа:  

$order = \Bitrix\Sale\Order::load($orderId);

/\*\*

\* получить коллекцию свойств заказа

\* @var Bitrix\Sale\PropertyValue $propertyCollection

\*/

$propertyCollection = $order->getPropertyCollection();

// получить свойства в виде массива

$arProperties = $propertyCollection->getArray();

// получить свойство по ID

$propValue = $propertyCollection->getItemByOrderPropertyId($propertyId);

/\*\*

\* получить значение свойства

\* @var Bitrix\Sale\PropertyValue $value

\*/

$value = $propValue->getValue();

// установить значение свойства

$propValue->setValue("value");

// чтобы сохранить изменения  
$order->save();

Для работы со значениями свойств заказа также можно использовать устаревший класс [CSaleOrderPropsValue](https://dev.1c-bitrix.ru/api_help/sale/classes/csaleorderpropsvalue/) со следующим набором функций:  

* [CSaleOrderPropsValue::GetList](https://dev.1c-bitrix.ru/api_help/sale/classes/csaleorderpropsvalue/csaleorderpropsvalue__getlist.52da0d54.php) ;
* [CSaleOrderPropsValue::GetByID](https://dev.1c-bitrix.ru/api_help/sale/classes/csaleorderpropsvalue/csaleorderpropsvalue__getbyid.54043fd5.php) ;
* [CSaleOrderPropsValue::Update](https://dev.1c-bitrix.ru/api_help/sale/classes/csaleorderpropsvalue/csaleorderpropsvalue__update.4d3a46b6.php) ;
* [CSaleOrderPropsValue::Add](https://dev.1c-bitrix.ru/api_help/sale/classes/csaleorderpropsvalue/csaleorderpropsvalue__add.af505780.php) ;
* [CSaleOrderPropsValue::GetOrderProps](https://dev.1c-bitrix.ru/api_help/sale/classes/csaleorderpropsvalue/csaleorderpropsvalue__getorderprops.af7c248d.php) .

Пример работы со значениями свойств заказа функциями устаревшего класса:  

// прочитать значение

$rsProp = CSaleOrderProps::GetList(

array(

"SORT" => "ASC",

),

array(

"PERSON\_TYPE\_ID" => $arOrder["PERSON\_TYPE\_ID"],

"CODE" => "PHONE",

)

);

// обновить значение

CSaleOrderPropsValue::Update(

$arVals['ID'],

array(

"ORDER\_ID" => $arVals['ORDER\_ID'],

"VALUE" => "140",

)

);

#### События изменения значений

События, связанные с изменением свойств заказов:  

* [\Bitrix\Sale\Order::onPropertyValueCollectionModify](https://dev.1c-bitrix.ru/api_d7/bitrix/sale/order/onpropertyvaluecollectionmodify.php) (для D7 методов изменение значений свойств);
* [OnBeforeSalePropertyValueSetField](https://dev.1c-bitrix.ru/api_d7/bitrix/sale/events/sale_setfields.php) (перед изменением поля);
* [OnSalePropertyValueSetField](https://dev.1c-bitrix.ru/api_d7/bitrix/sale/events/sale_setfields.php) (непосредственно перед изменением поля);
* [OnSaleComponentOrderProperties](https://dev.1c-bitrix.ru/api_help/sale/events/events_components.php) (после формирования списка свойств).

Есть и [другие события заказа](https://dev.1c-bitrix.ru/api_d7/bitrix/sale/events/index.php) , на которых можно работать со свойствами.  

## Интеграция с 1С

Для [обмена данными с 1С](https:///1c/integration/) на сайте используются профили обмена, в которых настраивается соответствие полей.  
![Настройка полей для экспорта в 1С](/upload/medialibrary/dc2/dc212d7297ce7044fffed625eb0e7547.png.webp)  

### Как добавить реквизит

На странице настройки интеграции 1С по пути Рабочий стол > Магазин > Настройки > Интеграция с 1С > Профили обмена есть возможность настроить параметры для выгрузки данных [из 1С на сайт](https:///dev/) .  

Если появилась необходимость помимо стандартных параметров добавить собственные, на этой же странице, ниже расположен раздел «1С: Дополнительные параметры», где задаются дополнительные параметры. ![Настройка реквизитов в 1С: Дополнительные параметры](/upload/medialibrary/989/9895a0fc2094ced7be201ef47f5d4223.png.webp)  

### Доступные типы

При помощи типов параметров можно определить какие данные ожидается получить и в какое свойство.  

Доступны следующие типы:  

* Значение;
* Пользователь;
* Заказ;
* Свойство заказа;
* Оплата;
* Отгрузка;
* Компания.

![Доступные типы параметров](/upload/medialibrary/124/124a79c01feab0b34db806fe2b9c45ce1.png.webp)  

#### Как добавить свой тип

Нет возможности расширения.  

#### API для работы со значениями

Так как все значения прилетают [из 1C](https:///1c/) , то API для работы с этими параметрами не предусмотрено.  

#### События изменения значений

Событий изменения значений не предусмотрено.  

## Элементы инфоблоков

Инфоблоки — основная сущность для хранения произвольной информации в [Битриксе](https:///dev/) . Именно инфоблоки используются для создания каталогов интернет-магазина. Таким образом, всё сказанное про свойства элементов в этом разделе справедливо и для свойств товаров.  
![](/upload/medialibrary/8fa/8faadfac23f60920a2d34185de566622.png.webp)  

### Как создать новое свойство

Свойства элементов инфоблока добавляются в настройках инфоблока: Рабочий стол > Контент > Инфоблоки > Типы инфоблоков > [Название типа] > [Название инфоблока] > вкладка «Свойства». Можно добавить неограниченное количество свойств (только для Инфоблоков 1.0).  
![Создание новых свойств в информационных блоках](/upload/medialibrary/83e/83eca7a8d518bf99b6cdf69633c1c426.png.webp)  
Здесь же можно задать сортировку свойств, в порядке которой свойства будут выводится в административной части при редактировании элемента и в каком порядке будут располагаться в массиве результатов компонента. По умолчанию сортировка свойств равна 500.  

### Доступные типы

При добавлении свойств доступен список базовых и пользовательских типов данных:  

|  |  |  |
| --- | --- | --- |
| Свойство | Базовое? | Код |
| Строка | Да | S |
| Число | Да | N |
| Список | Да | L |
| Файл | Да | F |
| Привязка к элементам ИБ | Да | E |
| Привязка к разделам ИБ | Да | G |
| HTML/текст | Нет | S:HTML |
| Видео | Нет | S:video |
| Дата | Нет | S:Date |
| Дата/Время | Нет | S:DateTime |
| Деньги | Нет | S:Money |
| Привязка к Яндекс.Карте | Нет | S:map\_yandex |
| Привязка к карте Google Maps | Нет | S:map\_google |
| Привязка к пользователю | Нет | S:UserID |
| Привязка к разделам с автозаполнением | Нет | G:SectionAuto |
| Привязка к теме форума | Нет | S:TopicID |
| Привязка к товарам (SKU) | Нет | E:SKU |
| Привязка к файлу (на сервере) | Нет | S:FileMan |
| Привязка к элементам в виде списка | Нет | E:EList |
| Привязка к элементам по XML\_ID | Нет | S:ElementXmlID |
| Привязка к элементам с автозаполнением | Нет | E:EAutocomplete |
| Справочник | Нет | S:directory |
| Счетчик | Нет | N:Sequence |

![Доступные типы данных](/upload/medialibrary/80c/80c652985bd2ddada9e7b6592d05b906.png.webp)  
Если вам потребуется создать boolean-свойство, например, «Да/Нет», то для этого нужно создать кастомное свойство в виде checkbox (флажок), унаследованное от свойства number (число). И задать логику, например, если флажок установлен возвращает число «1», соответственно, если не задано — вернет пустое значение.  
![Настройка активности свойства](/upload/medialibrary/439/439e780e9d6e63ab6659c6b12ea5943a.png.webp)  

#### Как добавить свой тип

Стандартных свойств довольно много, но если мощности Битрикса не хватает, можно создать собственное свойство с произвольным поведением.  

Например, можно создать свойство «Видео», которое позволяет хранить видеофайлы или ссылку на youtube-видео, предварительно загружая обложку.  
![Добавление видео из YouTube](/upload/medialibrary/eb2/eb2259296a3a02099421bd388a465962.png.webp)  
Создается кастомный тип свойства на обработчике события [OnIBlockPropertyBuildList](https://dev.1c-bitrix.ru/api_help/iblock/events/OnIBlockPropertyBuildList.php) модуля iblock. Пример создания кастомного свойства:  

AddEventHandler("iblock", "OnIBlockPropertyBuildList", array("IblockCustom", "GetUserTypeDescription"));

class IblockCustom

{

public static function GetUserTypeDescription()

{

return array(

"PROPERTY\_TYPE" => "S",

"USER\_TYPE" => "stringDate",

"DESCRIPTION" => "Дата (custom)",

"GetPublicViewHTML" => array(\_\_CLASS\_\_,"GetPublicViewHTML"),

"GetPublicEditHTML" => array(\_\_CLASS\_\_,"GetPublicEditHTML"),

"GetAdminListViewHTML" => array(\_\_CLASS\_\_,"GetAdminListViewHTML"),

"GetPropertyFieldHtml" => array(\_\_CLASS\_\_,"GetPropertyFieldHtml"),

"CheckFields" => array(\_\_CLASS\_\_,"CheckFields"),

"ConvertToDB" => array(\_\_CLASS\_\_,"ConvertToDB"),

"ConvertFromDB" => array(\_\_CLASS\_\_,"ConvertFromDB"),

"GetSettingsHTML" => array(\_\_CLASS\_\_,"GetSettingsHTML"),

"GetAdminFilterHTML" => array(\_\_CLASS\_\_,"GetAdminFilterHTML"),

"GetPublicFilterHTML" => array(\_\_CLASS\_\_,"GetPublicFilterHTML"),

"AddFilterFields" => array(\_\_CLASS\_\_,"AddFilterFields"),

);

}

}

Также существует возможность изменить отображение созданного типа свойства. Указанный параметр "PROPERTY\_TYPE" => "S" говорит о том, что новый тип свойства будет унаследован от строки, то есть отображаться он будет как строка. При желании изменить отображение, например, в панели администратора, понадобится переопределить в созданном классе следующие функции:

// Отображение в списке элементов

function GetPublicViewHTML($arProperty, $value, $strHTMLControlName)

{

return Loc::GetMessage($value['VALUE'] ? 'IBLOCK\_PROP\_CHECKBOX\_YES' : 'IBLOCK\_PROP\_CHECKBOX\_NO');

}

// Отображение при редактировании элемента

function GetPropertyFieldHtml($arProperty, $value, $strHTMLControlName)

{

return '<input type="hidden" name="' . $strHTMLControlName['VALUE'] . '" value="" /><input type="checkbox" name="'

. $strHTMLControlName['VALUE'] . '" value="1" ' . (intval($value['VALUE']) ? 'checked="checked"' : '').'/>';

}

Как создать кастомный тип свойства подробно можно узнать в курсе [Разработчик Bitrix Framework](https://dev.1c-bitrix.ru/learning/course/?COURSE_ID=43&LESSON_ID=2832) . Важнее всего здесь объявить метод [GetUserTypeDescription](https://dev.1c-bitrix.ru/api_help/iblock/classes/user_properties/GetUserTypeDescription.php) .  

#### API для работы со значениями

При необходимости изменения и получения значений свойств используются следующие функции класса [CIBlockElement](https://dev.1c-bitrix.ru/api_help/iblock/classes/ciblockelement) :  

* [CIBlockElement::GetProperty](https://dev.1c-bitrix.ru/api_help/iblock/classes/ciblockelement/getproperty.php) ;
* [CIBlockElement::SetPropertyValues](https://dev.1c-bitrix.ru/api_help/iblock/classes/ciblockelement/setpropertyvalues.php) ;
* [CIBlockElement::SetPropertyValuesEx](https://dev.1c-bitrix.ru/api_help/iblock/classes/ciblockelement/setpropertyvaluesex.php) ;
* [CIBlockElement::SetPropertyValueCode](https://dev.1c-bitrix.ru/api_help/iblock/classes/ciblockelement/setpropertyvaluecode.php) ;
* [CIBlockElement::Add](https://dev.1c-bitrix.ru/api_help/iblock/classes/ciblockelement/add.php) ;
* [CIBlockElement::Update](https://dev.1c-bitrix.ru/api_help/iblock/classes/ciblockelement/update.php) .

SetPropertyValuesEx и SetPropertyValues легко перепутать. Хороший программист знает в чём разница. Оба метода обновляют свойства, которые им передали. Но пропущенные свойства SetPropertyValues обнуляет, а SetPropertyValuesEx не трогает.  

Методы SetProperty\* не сбрасывают кеш инфоблока, в отличие от Add и Update. Если необходимо, кэш нужно сбросить вручную:  

// обновить значение

\CIBlockElement::SetPropertyValuesEx($arElement["ID"], $arElement["IBLOCK\_ID"], array("NEWS\_ID" => $propValue));

// сбросить кеш

$CACHE\_MANAGER->ClearByTag("iblock\_id\_" . $iblockId);

#### События изменения значений

При использовании этих функций запускаются следующие обработчики события, на которых можно изменить значение:  

* [OnIBlockElementSetPropertyValues](https://dev.1c-bitrix.ru/api_help/iblock/events/oniblockelementsetpropertyvalues.php) ,
* [OnIBlockElementSetPropertyValuesEx](https://dev.1c-bitrix.ru/api_help/iblock/events/oniblockelementsetpropertyvaluesex.php) ;
* [OnBeforeIBlockElementAdd](https://dev.1c-bitrix.ru/api_help/iblock/events/onbeforeiblockelementadd.php) ;
* [OnStartIBlockElementUpdate](https://dev.1c-bitrix.ru/api_help/iblock/events/OnStartIBlockElementUpdate.php) .

Остальные обработчики события модуля iblock представлены в [документации Bitrix](https://dev.1c-bitrix.ru/api_help/iblock/events/index.php) .  

## Товары в корзине и заказе

![Редактирование Состава заказа](/upload/medialibrary/fcd/fcd623d0fbc85906e94a7217437c374a.png.webp)  

### Как создать новое свойство

При добавлении товара в корзину есть возможность передавать его свойства: размер, цвет, производитель, длина, ширина и т.п. Свойства можно взять как из самого товара или SKU, так и создать «на лету».  

Если используется стандартный шаблон каталога, такие свойства передаются при настройке параметров компонента.  
![Настройка Параметров компонента Добавление в корзину](/upload/medialibrary/bb7/bb7d66b844512d385ab92d22af63e62b.png.webp)  
Характеристики товара, добавляемые в корзину — это свойства товара, которые попадут в корзину вместе с товаром. Свойства предложений, добавляемые в корзину — это свойства торговых предложений, которые попадут в корзину при добавлении торгового предложения.  

### Типы свойств

Все значения свойств хранятся в типе данных «строка».  

#### Как добавить свой тип

Возможности создать свой тип свойств нет. Но, так как данные хранятся в виде строки, обычно это не является проблемой.  

#### API для работы со значениями

Значения задаются при добавлении товара в корзину — [\Bitrix\Catalog\Product\Basket::addProduct](https://dev.1c-bitrix.ru/api_d7/bitrix/catalog/product/basket/addproduct.php) ( [Add2BasketByProductID](https://dev.1c-bitrix.ru/api_help/catalog/basket.php#add2basketbybroductid) в старом ядре).  

\Bitrix\Catalog\Product\Basket::addProduct и Add2BasketByProductID качестве третьего аргумента принимают массив, содержащий перечень свойств товара, добавленного в корзину. Для каждого свойства задается код, название и значение.  

// новый метод ядра D7

\Bitrix\Catalog\Product\Basket::addProduct(array(

'PRODUCT\_ID' => $productId,

'QUANTITY' => 1,

'PROPS' => array(

array(

"NAME" => "Цвет",

"CODE" => "COLOR",

"VALUE" => "Черный",

),

array(

"NAME" => "Размер",

"CODE" => "SIZE",

"VALUE" => "41",

),

)

));

// устаревший метод

Add2BasketByProductID($productId, 1,

array(

array(

"NAME" => "Цвет",

"CODE" => "COLOR",

"VALUE" => "Черный",

),

array(

"NAME" => "Размер",

"CODE" => "SIZE",

"VALUE" => "41",

),

)

);

Тогда в административном интерфейсе Магазин > Покупатели > Корзины можно посмотреть какие товары и с какими свойствами были добавлены.  
![Свойства товаров в корзине](/upload/medialibrary/544/5440966688004e42940b5bbcab13e5df.png.webp)  
В документации Bitrix дана более подробная инструкция по использованию функций [Add2BasketByProductID](https://dev.1c-bitrix.ru/api_help/catalog/basket.php#add2basketbybroductid) и [\Bitrix\Catalog\Product\Basket::addProduct](https://dev.1c-bitrix.ru/api_d7/bitrix/catalog/product/basket/addproduct.php) .  
Получить или изменить свойства и их значения можно с помощью следующих функций класса [CSaleBasket](https://dev.1c-bitrix.ru/api_help/sale/classes/csalebasket) :  

* [CSaleBasket::GetPropsList](https://dev.1c-bitrix.ru/api_help/sale/classes/csalebasket/csalebasket__getpropslist.e03206e8.php) ;
* [CSaleBasket::Update](https://dev.1c-bitrix.ru/api_help/sale/classes/csalebasket/csalebasket__update.3dd628d0.php) .

Пример использования функции Update:  

CSaleBasket::Update($id, array(

"PROPS" => array(

"NAME" => "Новый товар",

"CODE" => "IS\_NEW",

"VALUE" => $value,

),

));

#### События изменения значений

Для изменения значений свойств можно воспользоваться следующими обработчиками событий:  

* OnBeforeBasketAdd;
* OnBeforeBasketUpdate.

В документации Bitrix также можно найти другие [обработчики события](https://dev.1c-bitrix.ru/api_help/sale/events/events_basket.php) , которые вам помогут в реализации решений.  

## Компоненты

![Настройка карты Google](/upload/medialibrary/b80/b80f7912465642eaf70fc33b285d70dd.png.webp)  

### Как добавить параметр

Для добавления параметров в окно настройки компонента используется файл .parameters.php. В нём разработчик компонента/шаблона компонента должен описать массив параметров.  

В курсе [Разработчик Bitrix Framework](https://dev.1c-bitrix.ru/learning/course/?COURSE_ID=43&LESSON_ID=2132) дается инструкция как нужно добавлять параметры.  

### Доступные типы параметров

В настройках параметров компонентов для отображения параметров доступны следующие типы:  

* список (LIST);
* строка (STRING);
* флажок (CHECKBOX);
* палитра (COLORPICKER).

![Настройка цветов](/upload/medialibrary/6f4/6f4414baa51d0d17acee2fa8d4365067.png.webp)  
Параметр компонента типа COLORPICKER  

#### Как добавить свой тип

Для создания собственных типов указывается TYPE=CUSTOM и три параметра JS\_FILE, JS\_EVENT и JS\_DATA.  

$arComponentParameters = array(

"PARAMETERS" => array(

'PATH\_TO\_FILE' => array(

'NAME' => 'Путь до файла',

'TYPE' => 'CUSTOM',

'JS\_FILE' => '/local/components/intervolga.test/supercomponent/settings/settings.js',

'JS\_EVENT' => 'OnSettingEdit',

'JS\_DATA' => '',

'PARENT' => 'BASE',

),

)

);

JS\_FILE - указывается путь до JS файла, который отвечает за отображение параметра  
JS\_EVENT - указывается callback-функция, которая будет вызвана после подключения  
JS\_FILE JS\_DATA - указываются параметры, которые будут переданы в callback-функцию  

Пример собственного типа параметра компонента:  
![Параметры компонента Суперкомпонент](/upload/medialibrary/4a4/4a41f538726cb00aff145ef1b34ff744.png.webp)  
Подробная инструкция по созданию параметра с кастомизированным типов указана в курсе [Разработчик Bitrix Framework](https://dev.1c-bitrix.ru/learning/course/?COURSE_ID=43&LESSON_ID=4880) .  

#### API для работы со значениями

API для работы со значениями не предусмотрено.  

#### События изменения значений

Событий изменения значений не предусмотрено.  

## Умный фильтр

![Пример умного фильтра в Битрикс](/upload/medialibrary/e43/e43ab38f062e5327ae223fe45f2d412e.png.webp)  

### Как добавить новое свойство

Настройка свойств, которые отображаются в умном фильтре производится в настройках свойств инфоблока или в свойствах товаров (Рабочий стол > Магазин > [Название инфоблока] > Свойства товаров). О них мы говорили выше.  
![Добавление свойств к товарам](/upload/medialibrary/ec3/ec33162402eae561c07a488b168f3026.png.webp)  
В параметрах конкретного свойства можно включить свойство в умный фильтр и настроить в каком виде он будет отображаться.  
![Включение Умного фильтра](/upload/medialibrary/751/751e18dd9a081451d3582108ba8cc0f9.png.webp)  
Если свойств в инфоблоке каталога много, то проще это сделать на странице административного интерфейса Рабочий стол > Магазин > [Название инфоблока] > Настройки каталога ![Настройка отображения свойств элементов](/upload/medialibrary/9cd/9cdbe885b95832c67e2936e846c36d8c.png.webp)  
На этой странице отображаются все свойства, которые имеются в инфоблоке каталога и в инфоблоке SKU, соответственно здесь можно произвести их настройку.  

Есть возможность настроить разные свойства в разных разделах каталога (Рабочий стол > Магазин > [Название инфоблока] > Разделы) ![Настройка отображения свойств элементов](/upload/medialibrary/f0d/f0d35f6bf5f7f67a60f171d2b4d48184.png.webp)  

### Доступные типы

Умный фильтр предлагает разные варианты отображения в зависимости от типа свойства товара:  

* «Справочник» может отображаться как флажки, радио кнопки и выпадающий список (интересный вариант — список с картинками):

![Отображение Умного фильтра: Справочник](/upload/medialibrary/5dc/5dc0a51845a30b9acc8286fce12ba03b.jpg.webp)  

* «Число» отображается в виде двух полей «от-до»:

![Отображение Умного фильтра: Число](/upload/medialibrary/6b1/6b12cbe714db98342f0ae2fc8ae264f7.png.webp)  

* Остальные типы отображаются как флажки, радио кнопки и выпадающий список:

![Отображение Умного фильтра: Флажок](/upload/medialibrary/5fc/5fcb9d1e6b5046bda58f1f058037187e.png.webp)  

#### Как добавить свой тип

Добавить свой вариант отображения в настройки умного фильтра нельзя. Если какое-то поле требует особого отображения, то дорабатывается шаблон компонента «Умный фильтр».  

#### API для работы со свойствами в умном фильтре

Настроить вывод свойства в умном фильтре (во всех разделах или в каком-то конкретном) позволяет класс [\Bitrix\Iblock\SectionPropertyTable](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/sectionpropertytable/index.php) :  

* \Bitrix\Iblock\SectionPropertyTable::add;
* \Bitrix\Iblock\SectionPropertyTable::getList;
* \Bitrix\Iblock\SectionPropertyTable::update;
* \Bitrix\Iblock\SectionPropertyTable::delete.

Пример использования функций:  

// вывод свойств раздела инфоблока

$sectionProperties = \Bitrix\Iblock\SectionPropertyTable::getList(

array(

'filter' => array(

'SECTION\_ID' => $sectionId,

'IBLOCK\_ID' => $iblockId,

),

)

);

// включение свойства в умный фильтр раздела

$data = array(

'fields' => array(

'SECTION\_ID' => $sectionId,

'IBLOCK\_ID' => $iblockId,

'PROPERTY\_ID' => $property['ID'],

'DISPLAY\_TYPE' => $property['PROPERTY\_TYPE'],

),

);

\Bitrix\Iblock\SectionPropertyTable::add($data);

При добавлении свойства в умный фильтр нужно указать ID раздела каталога, в котором оно должно отображаться. Если раздел не задать, свойство появится в умном фильтре всех разделов каталога.  

#### События изменения значений

* \Bitrix\Iblock\SectionProperty::onBeforeAdd;
* \Bitrix\Iblock\SectionProperty::onAdd;
* \Bitrix\Iblock\SectionProperty::onAfterAdd;
* \Bitrix\Iblock\SectionProperty::onBeforeUpdate;
* \Bitrix\Iblock\SectionProperty::onUpdate;
* \Bitrix\Iblock\SectionProperty::onAfterUpdate;
* \Bitrix\Iblock\SectionProperty::onBeforeDelete;
* \Bitrix\Iblock\SectionProperty::onDelete;
* \Bitrix\Iblock\SectionProperty::onAfterDelete.

## Страницы и разделы сайта

Свойства есть даже на обычных страницах и разделах сайта. Два из них созданы по умолчанию и используются для поисковиков: description и keywords. Свойства страниц и разделов расширяемы, но их значения хранятся в виде строки.  
![Заполнение свойств страницы](/upload/medialibrary/ce9/ce937af7d62fb508462dad89993afb52.png.webp)  

### Как создать новое свойство

Если свойство должно работать на всех страницах сайта и разделах сайта, добавить его можно в настройках Рабочий стол > Настройки > Настройки продукта > Настройки модулей > Управление структурой ![Создание нового свойства](/upload/medialibrary/cd3/cd35fd4f2ca6adaa66ae4f16d32d78f3.png.webp)  
Свойство для раздела или страницы можно задать с публичной части сайта:  
![Изменение Заголовков и свойств страницы через Публичную часть](/upload/medialibrary/535/5358bab2e21edbddae89db65f4bcc88a.png.webp)  

### Типы свойств

Все свойства имеют тип данных «строка».  

#### Как добавить свой тип

Такой возможности нет.  

#### API для работы со значениями

Для работы со свойствами страниц/разделов используется класс [CMain](https://dev.1c-bitrix.ru/api_help/main/reference/cmain) . Вот некоторые из часто применяемых функции:  

* [CMain::ShowProperty](https://dev.1c-bitrix.ru/api_help/main/reference/cmain/showproperty.php) (отображение свойств с помощью технологии отложенных функций);
* [CMain::GetProperty](https://dev.1c-bitrix.ru/api_help/main/reference/cmain/getproperty.php) (возвращает значение свойства);
* [CMain::SetPageProperty](https://dev.1c-bitrix.ru/api_help/main/reference/cmain/setpageproperty.php) (устанавливает свойство страницы);
* [CMain::SetDirProperty](https://dev.1c-bitrix.ru/api_help/main/reference/cmain/setdirproperty.php) (устанавливает свойство раздела).

Пример использования функций GetProperty и SetPageProperty:  

// установить значение свойства страницы

$APPLICATION->SetPageProperty("keywords", "свойства, bitrix");

// получить значение свойства страницы

$APPLICATION->GetProperty("keywords");

// вывести значение свойства страницы

<title><?$APPLICATION->ShowProperty("keywords")?></title>

При использовании функции GetProperty программисту важно понимать как работают отложенные функции.  

Как работать со свойствами страницы/разделов и какие функции применяются, описано в курсе [Разработчик Bitrix Framework](https://dev.1c-bitrix.ru/learning/course/?COURSE_ID=43&LESSON_ID=2814) .  

#### События изменения значений

Событий изменения значений не предусмотрено.  

## Пункты меню

Если в меню сайта какие-то пункты должны отличаться от остальных, в этом помогут параметры пунктов меню. Например, если понадобится, чтобы один из пунктов меню был другого цвета. ![Изменение Пунктов меню](/upload/medialibrary/81a/81aa7c8d9b5c61db4854ff5b723267fd.png.webp)  

### Как добавить и изменить параметр

Параметры меню можно задать через административный интерфейс. Для этого по пути Рабочий стол > Контент > Структура сайта > Файлы и папки нужно отыскать файл меню и перейти в режим редактирования меню в расширенном режиме.  
![Добавление и изменение параметров Меню](/upload/medialibrary/842/842711c3532c032771d456a5acbcbf93.png.webp)  

### Доступные типы

Все свойства имеют тип данных «строка».  

Как добавить свой тип.  

Такой возможности нет.  

#### Как получить значение

Получить значение параметра можно через массив PARAMS шаблона компонента «меню».  
![Использование массива PARAMS](/upload/medialibrary/9bc/9bc46d68fe299af30d12d55460e0dd00.png.webp)  
Подробный обзор полей меню описан [в документации Bitrix](https://dev.1c-bitrix.ru/user_help/content/fileman/fileman/fileman_menu_edit.php#edit_full) .  

#### События изменения значений

Событий изменения значений не предусмотрено.  

## Универсальное решение — пользовательские поля (UF)

Расширение полей в Битриксе помимо стандартных свойств делается также с помощью UF полей.  
![Дополнительные поля в Битрикс](/upload/medialibrary/6c3/6c392c26328541422c23cce20a2c4083.png.webp)  

### Как создать новое свойство

Все UF свойства в Битриксе отображаются на странице «Пользовательские поля» административного интерфейса по пути Рабочий стол > Настройки > Настройки продукта > Пользовательские поля.  

Пользовательские поля можно создать для любой записи в Битрикс, если у неё есть числовой ID. Визуальный интерфейс же есть лишь для немногих сущностей: пользователи, разделы ИБ, склады, блоги, форумы. ![Создание пользовательских полей](/upload/medialibrary/4f9/4f94f4146c7d6d1a756910b7b1b2c0c1.png.webp)  
Для управления порядком отображения UF-свойств при редактировании конкретного свойства есть возможность установить порядок сортировки. Величина сортировки влияет на порядок вывода свойств в различных административных и публичных формах сайта.  

### Доступные типы

При добавлении UF свойства на выбор доступны следующие типы:  

|  |  |
| --- | --- |
| Свойство | Код |
| Письмо (email) | mail\_message |
| Деньги | money |
| Видео | video |
| Привязка к элементам highload-блоков | hlblock |
| Строка | string |
| Целое число | integer |
| Число | double |
| Дата со временем | datetime |
| Дата | date |
| Да/Нет | boolean |
| Адрес | address |
| Ссылка | url |
| Файл | file |
| Список | enumeration |
| Привязка к разделам инф. блоков | iblock\_section |
| Привязка к элементам инф. блоков | iblock\_element |
| Шаблон | string\_formatted |
| Опрос | vote |
| Содержимое ссылки | url\_preview |

Важное отличие от прочих свойств: после создания нельзя менять «множественность».  

#### Как добавить свой тип

Чтобы добавить свой тип свойства, необходимо создать обработчик события OnUserTypeBuildList и объявить класс, наследуемый от класса базового свойства. В унаследованном классе переопределить функцию GetUserDescription. Переопределите остальные методы, если это требуется.  

AddEventHandler("main", "OnUserTypeBuildList", array("UserTypeMediaLibrary", "GetUserTypeDescription"));

class UserTypeMediaLibrary extends \CUserTypeEnum

{

function GetUserTypeDescription()

{

return array(

"USER\_TYPE\_ID" => "cmedia",

"CLASS\_NAME" => "UserTypeMediaLibrary",

"DESCRIPTION" => "Привязка к коллекции медиабиблиотеки",

"BASE\_TYPE" => "enum",

);

}

}

После этого, в списке доступных типов появится новое свойство.  

#### API для работы со значениями

Добавление, чтение и обновление значений свойств происходит с помощью функций класса CUserTypeManager:  

* CUserTypeManager::Update;
* CUserTypeManager::Add;
* CUserTypeManager::GetUserFields.

Пример использования:  

global $USER\_FIELD\_MANAGER;

// получить все значения объекта

$arFields = $USER\_FIELD\_MANAGER->GetUserFields("USER");

// обновить значение UF свойства

$USER\_FIELD\_MANAGER->Update('USER', $arUser['ID'], array(

'UF\_FAVORITE' => $value

));

О том, как управлять UF свойствами более подробно описано в курсе [Разработчик Bitrix Framework](https://dev.1c-bitrix.ru/learning/course/?COURSE_ID=43&LESSON_ID=3496) .  

#### События изменения значений

События изменения значений UF свойств:  

* OnBeforeUserTypeAdd;
* OnAfterUserTypeAdd;
* OnBeforeUserTypeUpdate;
* OnAfterUserTypeUpdate;
* OnBeforeUserTypeDelete;
* OnAfterUserTypeDelete;
* OnUserTypeRightsCheck.

## Внешние сервисы местоположений

У местоположений Битрикса также есть поля, которые можно использовать как свойства, они называются «Внешние сервисы».  
![Внешние сервисы](/upload/medialibrary/0ae/0aef71400a43e50baff137a7b125715c.png.webp)  

### Как создать новое свойство

Внешние сервисы настраиваются на странице по пути: Рабочий стол > Магазин > Настройки > Местоположения > Внешние сервисы  
![Добавление сервисов](/upload/medialibrary/ee5/ee563df96ea8017cdb9978c018945c76.png.webp)  

### Доступные типы

Все свойства имеют тип данных «строка».  

#### Как добавить свой тип

Такой возможности нет.  

#### API для работы со значениями

Для того, чтобы работать со значениями внешних сервисов местоположении пользуйтесь следующими методами класса [\Bitrix\Sale\Location\LocationTable](https://dev.1c-bitrix.ru/api_d7/bitrix/sale/location/locationtable/) :  

* \Bitrix\Sale\Location\LocationTable::getList;
* \Bitrix\Sale\Location\LocationTable::getByCode;
* \Bitrix\Sale\Location\LocationTable::add;
* \Bitrix\Sale\Location\LocationTable::update;
* \Bitrix\Sale\Location\LocationTable::delete

Использование перечисленных функций подробно разобрано на примерах в курсе [Разработчик Bitrix Framework](https://dev.1c-bitrix.ru/learning/course/?COURSE_ID=43&LESSON_ID=3570) .  

#### События изменения значений

События, связанные с изменениями:  

* \Bitrix\Sale\Location\Location::OnBeforeAdd;
* \Bitrix\Sale\Location\Location::OnAdd;
* \Bitrix\Sale\Location\Location::OnAfterAdd;
* \Bitrix\Sale\Location\Location::OnBeforeUpdate;
* \Bitrix\Sale\Location\Location::OnUpdate;
* \Bitrix\Sale\Location\Location::OnAfterUpdate;
* \Bitrix\Sale\Location\Location::OnBeforeDelete;
* \Bitrix\Sale\Location\Location::OnDelete

## Заключение

Наиболее универсальные сущности в Битриксе: ИБ, HL-блоки. Для них можно добавить собственный тип свойства, менять его внешний вид. Вторые по удобству сущности: пользователи, задачи Б24, склады и т.п. У таких сущностей уже есть предназначение и мы можем их только дополнять UF-полями. Наименее гибкие сущности: пункты меню, страницы и разделы сайта. Свойств можно создать сколько угодно, но хранить в них можно только строки.  

### Делимся с самыми любознательными читателями сводной таблицей

[PDF версия этой таблицы](/upload/medialibrary/%D0%A1%D0%B2%D0%BE%D0%B9%D1%81%D1%82%D0%B2%D0%B0%20%D0%91%D0%B8%D1%82%D1%80%D0%B8%D0%BA%D1%81%20-%20%D0%A1%D0%B2%D0%BE%D0%B9%D1%81%D1%82%D0%B2%D0%B0%20%D0%91%D0%B8%D1%82%D1%80%D0%B8%D0%BA%D1%81.pdf)  

ИНТЕРВОЛГА — опытный веб-интегратор. Мы любим и умеем решать интересные и нестандартные задачи.  

Наши специалисты — сертифицированные профессионалы, которые знают все и даже больше о платформе БУС и не устают совершенствоваться.  

Пишите нам, и мы не только поможем разобраться со свойствами [1С-Битрикс](https:///dev/) , но и [обучим всем тонкостям работы с платформой](https://www.intervolga.ru/vacancy/developer/) .

Оцените статью

Empty

30.01.2019

Понравилась статья?

Поделитесь ссылкой с друзьями и коллегами!

### Статьи по теме

![](https://www.intervolga.ru/upload/resize_cache/iblock/72c/470_200_2/tuyd87zdorzwitrgbiy23e0tjwvelto6.jpg.webp?w=1920)

[Система лояльности в B2B-продажах: как создать и будут ли результаты](/blog/projects/sistema-loyalnosti-v-b2b-prodazhakh-kak-sozdat-i-budut-li-rezultaty/) В B2B-продажах клиенты ищут не просто продукт, а партнера, который поможет им решить их бизнес-проблемы. Привлечение и удержание клиентов — одна из ...

![](https://www.intervolga.ru/upload/resize_cache/iblock/43e/470_200_2/uxp2ez5pt78085puvl640v09dvz35svc.jpg.webp?w=1920)

[Создаем контент-хаб товарных данных на Pimcore](/blog/projects/sozdaem-kontent-khab-na-pimcore/) Наступит день, когда ваши 1С или БД сайта перестанут справляться с возросшим объемом товарного медиаконтента. Рассказываем как организовать правильное хранение ...

![](https://www.intervolga.ru/upload/resize_cache/iblock/4ac/470_200_2/v5x8l0zfvbhlx4voieruipfu7r9w35bj.jpg.webp?w=1920)

[Выжимаем максимум скорости из PHP](/blog/projects/vyzhimaem-maksimum-skorosti-iz-php/) Когда дело доходит до запуска PHP-приложений, выбор подходящего веб-сервера критически важен. Цель статьи — помочь в выборе оптимального решения для своих проек...

![](https://www.intervolga.ru/upload/resize_cache/iblock/a25/470_200_2/xgq29ifcvq6w7lq5imutud99rsgffjx9.png.webp?w=1920)

[Организация поиска на сайте: выбираем между поиском Битрикса, Sphinx и Elasticsearch](/blog/projects/organizatsiya-poiska-na-sayte-vybiraem-mezhdu-poiskom-bitriksa-sphinx-i-elasticsearch/) В статье разбираем популярные поисковые движки, чтобы выбрать лучший под задачи конкретного проекта. Даем советы по индексации каталога и построении «умного» фи...

![](https://www.intervolga.ru/upload/resize_cache/iblock/425/470_200_2/yz9mn3dr07ihnc5uhatfgvjn911yq80c.jpg.webp?w=1920)

[Доработка системы LMS Knomary](/blog/projects/dorabotka-sistemy-lms-knomary/) Must have для бизнеса, где главный актив это люди, — стратегия обучения и развития персонала. Рассказываем как помогли доработать LMS-систему для компании ЕВРАЗ...

![](https://www.intervolga.ru/upload/resize_cache/iblock/fb0/470_200_2/fci6sf0g1flr0qjsxk9ao4x1232kuihb.png.webp?w=1920)

[«Как раньше» больше не работает — B2B-система продаж сейчас](/blog/projects/kak-ranshe-bolshe-ne-rabotaet-b2b-sistema-prodazh-seychas/) В этой статье хотим поговорить с чем сейчас сталкивается оптовый бизнес (множеством вызовов и изменений, которые требуют адаптации, а также оптимизации процессо...

Мы работаем по одному из двух форматов:

* аренда команды (от 2 человек, не менее 3 месяцев);
* итерации с фиксированной ценой (1-3 месяца длительностью).

ИНТЕРВОЛГА предоставляет:

* регулярные онлайн-планерки с заказчиком;
* квалифицированных специалистов;
* организованную команду (находятся в одном помещении, что упрощает решение рабочих вопросов);
* полную прозрачность и регулярность отчетов о результатах.

Ключевые услуги:

* нагруженный интернет-магазин;
* личный кабинет;
* оптовые продажи — B2B-платформа;
* маркетплейс;
* технический аудит сайта;
* Битрикс24 — корпоративные HR-порталы;
* Битрикс24 — построение CRM-системы;
* Битрикс24 — личные кабинеты сотрудников;
* Битрикс24 — аудит портала;
* 1С — интеграция с другими системами;
* 1С — доработка системы;
* маркетинг — комплексное интернет-продвижение;
* маркетинг — продвижение для B2B.

Хотите получать лучшие статьи от INTERVOLGA раз в месяц?

Подпишитесь на рассылку — спамить не будем

[![intervolga.ru](/assets/logo/white.svg)](/)

* [Москва](/)
* [Волгоград](/volgograd/)
* [Ростов](/drugoe/rostov/)
* [Контакты](/contacts/)

* [+7 495 648 57 90](tel:+7%20495%20648%2057%2090)
* [+7 844 295 99 99](tel:+7%20844%20295%2099%2099)
* [info@intervolga.ru](mailto:info@intervolga.ru)

© 2003-2025, интернет-агентство INTERVOLGA

[Политика конфиденциальности](/privacy/)