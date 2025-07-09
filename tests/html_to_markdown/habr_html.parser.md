Все сервисы Хабра

[Сообщество IT-специалистов](/)   [Ответы на любые вопросы об IT](https://qna.habr.com?utm_source=habr&utm_medium=habr_top_panel)   [Профессиональное развитие в IT](https://career.habr.com?utm_source=habr&utm_medium=habr_top_panel)   [Удаленная работа для IT-специалистов](https://freelance.habr.com?utm_source=habr&utm_medium=habr_top_panel)

[Как стать автором](https://habr.com/sandbox/start/)

Мегапосты: [Боли сисадмина](https://u.tmtm.ru/u-k-p-270220) [От свайпа до фриланса](https://u.tmtm.ru/u-f-p-270220) [Подарки для Хабра](https://u.tmtm.ru/u-mv-t-210220)

* [Все потоки](https://habr.com/ru/all/)
* [Разработка](https://habr.com/ru/flows/develop/)
* [Научпоп](https://habr.com/ru/flows/popsci/)
* [Администрирование](https://habr.com/ru/flows/admin/)
* [Дизайн](https://habr.com/ru/flows/design/)
* [Менеджмент](https://habr.com/ru/flows/management/)
* [Маркетинг](https://habr.com/ru/flows/marketing/)

[Войти](https://habr.com/ru/auth/login/) [Регистрация](https://habr.com/ru/auth/register/)

[![](//habrastorage.org/getpro/habr/avatars/b79/4ae/4bc/b794ae4bcf85f36de7caa65b12c3ccab.png) neyronius](https://habr.com/ru/users/neyronius/ "Автор публикации")   12 июля 2012 в 12:47  

# Применение замыканий в PHP

* [PHP](https://habr.com/ru/hub/php/ "Вы не подписаны на этот хаб")

Введение в PHP 5.3 замыканий — одно из главных его новшеств и хотя после релиза прошло уже несколько лет, до сих пор не сложилось стандартной практики использования этой возможности языка. В этой статье я попробовал собрать все наиболее интересные возможности по применению замыканий в PHP.  

Для начала рассмотрим, что же это такое — замыкание и в чем его особенности в PHP.  

```
$g = 'test';

$c = function($a, $b) use($g){
    echo $a . $b .  $g;
};

$g = 'test2';

var_dump($c);

/*
object(Closure)#1 (2)
{
     ["static"]=> array(1) { ["g"]=> string(4) "test" } 
     ["parameter"]=> array(2) { 
          ["$a"] => string(10) "" 
          ["$b"]=> string(10) ""
      }
}
*/
```

Как видим, замыкание как и лямбда-функция представляют собой объект класса Closure, коорый хранит переданные параметры. Для того, чтобы вызывать объект как функцию, в PHP5.3 ввели магический метод \_\_invoke.  

```
function getClosure()
{
    $g = 'test';

    $c = function($a, $b) use($g){       
        echo $a . $b . $g;        
    };

    $g = 'test2';    

    return $c;
}

$closure = getClosure();
$closure(1, 3); //13test

getClosure()->__invoke(1, 3); //13test
```

Используя конструкцию use мы наследуем переменную из родительской области видимости в локальную область видимости ламбда-функции.  
Ситаксис прост и понятен. Не совсем понятно применение такого функционала в разработке web-приложений. Я просмотрел код нескольких совеременных фреймворков, использующих новые возможности языка и попытался собрать вместе их различные применения.  

#### Функции обратного вызова

Самое очевидное применение анонимных функций — использование их в качестве функций обратного вызова (callbacks). В PHP имеется множество стандартных функций, принимающих на вход тип callback или его синоним callable введенный в PHP 5.4. Самые популярные из них array\_filter, array\_map, array\_reduce. Функция array\_map служит для итеративной обработки элементов массива. Callback-функция применяется к каждому элементу массива и в качестве результата выдается обработанный массив. У меня сразу возникло желание сравнить производительность обычной обработки массива в цикле с применением встроенной функции. Давайте поэкспериментируем.  

```
$x = range(1, 100000);
$t = microtime(1);

$x2 = array_map(function($v){
    return $v + 1;
}, $x);
//Time: 0.4395
//Memory: 22179776
//---------------------------------------

$x2 = array();
foreach($x as $v){
    $x2[] = $v + 1;
}
//Time: 0.0764
//Memory: 22174788
//---------------------------------------

function tr($v){
    return $v + 1;
}
$x2 = array();
foreach($x as $v){
    $x2[] = tr($v);
}
//Time: 0.4451
//Memory: 22180604
```

Как видно, накладные расходы на большое количество вызовов функций дают ощутимый спад в производительности, чего и следовало ожидать. Хотя тест синтетический, задача обработки больших массивов возникает часто, и в данном случае применение функций обработки данных может стать тем местом, которе будет существенно тормозить ваше приложение. Будьте осторожны. Тем не менее в современных приложениях такой подход используется очень часто. Он позволяет делать код более лаконичным, особенно, если обработчик объявляется где-то в другом месте, а не при вызове.  

По сути в данном контексте применение анонимных функций ничем не отличается от старого способа передачи строкового имени функции или callback-массива за исключением одной особенности — теперь мы можем использовать замыкания, то есть сохранять переменные из области видимости при создании функции. Рассмотрим пример обработки массива данных перед добавлением их в базу данных.  

```
//объявляем функцию квотирования.
$quoter = function($v) use($pdo){
	return $pdo->quote($v);//использовать эту функцию не рекомендуется, тем не менее :-)
}
$service->register(‘quoter’, $quoter);
…
//где-то в другом месте
//теперь у нас нет доступа к PDO
$data = array(...);//массив строк
$data = array_map($this->service->getQuoter(), $data);
//массив содержит обработанные данные.
```

Очень удобно применять анонимные функции и для фильтрации  

```
$x = array_filter($data, function($v){ return $v > 0; });
//vs
$x = array();
foreach($data as $v)
{
	if($v > 0){$x[] = $v}
}
```

#### События.

Замыкания идеально подходят в качестве обработчиков событий. Например  

```
//где-то при конфигурации приложения.
$this->events->on(User::EVENT_REGISTER, function($user){
	//обновить счетчик логинов для пользователя и т.д.
});

$this->events->on(User::EVENT_REGISTER’, function($user){
	//выслать email для подтверждения.
});

//в обработчике формы регистрации
$this->events->trigger(User::EVENT_REGISTER, $user);
```

Вынос логики в обработчики событий с одной стороны делает код более чистым, с другой стороны — усложняет поиск ошибок — поведение системы иногда становится неожиданным для человека, который не знает, какие обработчики навешаны в данный момент.  

#### Валидация

Замыкания по сути сохраняют некоторую логику в переменной, которая может быть выполнена или не выполнена в по ходу работы скрипта. Это то, что нужно для реализации валидаторов:  

```
$notEmpty = function($v){ return strlen($v) > 0 ? true : “Значение не может быть пустым”; };
$greaterZero = function($v){ return $v > 0 ? true : “Значение должно быть больше нуля”; };

function getRangeValidator($min, $max){
	return function($v) use ($min, $max){
		return ($v >= $min && $v <= $max) 
                         ? true 
                         : “Значение не попадает в промежуток”;
	};
}
```

В последнем случае мы применяем функцию высшего порядка, которая возвращает другую функцию — валидатор с предустановленными границами значений. Применять валидаторы можно, например, так.  

```
class UserForm extends BaseForm{

    public function __constructor()
    {
        $this->addValidator(‘email’, Validators::$notEmpty);
        $this->addValidator(‘age’, Validators::getRangeValidator(18, 55));
        $this->addValidator(‘custom’, function($v){
		//some logic
        });
    }

    /**
    * Находится в базовом классе.
    */
    public function isValid()
    {
        …
        $validationResult = $validator($value);
        if($validationResult !== true){
            $this->addValidationError($field, $validationResult);
        }
        …
    }
}
```

Использование в формах классический пример. Также валидация может использоваться в сеттерах и геттерах обычных классов, моделях и т.д. Хорошим тоном, правда, считается декларативная валидация, когда правила описаны не в форме функций, а в форме правил при конфигурации, тем не менее, иногда такой подход очень кстати.  

#### Выражения

В Symfony встречается очень интересное применение замыканий. Класс [ExprBuilder](https://github.com/symfony/symfony/blob/master/src/Symfony/Component/Config/Definition/Builder/ExprBuilder.php) опеделяет сущность, которая позволяет строить выражения вида  

```
...
->beforeNormalization()
    ->ifTrue(function($v) { return is_array($v) && is_int(key($v)); })
    ->then(function($v) { return array_map(function($v) { return array('name' => $v); }, $v); })
 ->end()
...
```

В Symfony как я понял это внутренний класс, который используется для создания обработки вложенных конфигурационных массивов (поправьте меня, если не прав). Интересна идея реализации выражений в виде цепочек. В принципе вполне можно реализовать класс, который бы описывал выражения в таком виде:  

```
$expr = new Expression();

$expr
->if(function(){ return $this->v == 4;})
->then(function(){$this->v = 42;})
->else(function(){})
	->elseif(function(){})
->end()
->while(function(){$this->v >=42})
	->do(function(){
		$this->v --;
})
->end()
->apply(function(){/*Some code*/});

$expr->v = 4;
$expr->exec();
echo $expr->v;
```

Применение, конечно, экспериментально. По сути — это запись некоторого алгоритма. Реализация такого функционала достаточно сложна — выражение в идеальном случае должно хранить дерево операций. Инетересна концепция, может быть где-то такая конструкция будет полезна.  

#### Роутинг

Во многих мини-фреймворках роутинг сейчас работает на анонимных функциях.  

```
App::router(‘GET /users’, function() use($app){
    $app->response->write(‘Hello, World!’);
});
```

Достаточно удобно и лаконично.  

#### Кеширование

На хабре это уже обсуждалось, тем не менее.  

```
$someHtml = $this->cashe->get(‘users.list’, function() use($app){
	$users = $app->db->table(‘users)->all();
	return $app->template->render(‘users.list’, $isers);
}, 1000);
```

Здесь метод get проверяет валидность кеша по ключу ‘users.list’ и если он не валиден, то обращается к функции за данными. Третий параметр определяет длительность хранения данных.  

#### Инициализация по требованию

Допустим, у нас есть сервис Mailer, который мы вызываем в некоторых методах. Перед использованием он должен быть сконфигурирован. Чтобы не инициализировать его каждый раз, будем использовать ленивое создание объекта.  

```
//Где-то в конфигурационном файле.
$service->register(‘Mailer’, function(){
	return new Mailer(‘user’, ‘password’, ‘url’);
});

//Где-то в контроллере
$this->service(‘Mailer’)->mail(...);
```

Инициализация объекта произойдет только перед самым первым использованием.  

#### Изменение поведения объектов

Иногда бывает полезно переопределить поведение объектов в процессе выполнения скрипта — добавить метод, переопределить старый, и т.д. Замыкание поможет нам и здесь. В PHP5.3 для этого нужно было использовать различные обходные пути.  

```
class Base{

    public function publicMethod(){echo 'public';}
    private function privateMethod(){echo 'private';}    
    //будем перехватывать обращение к замыканию и вызывать его.
    public function __call($name, $arguments) {
        if($this->$name instanceof Closure){
            return call_user_func_array($this->$name, array_merge(array($this), $arguments));
        }
    }
}

$b = new Base; 

//создаем новый метод
$b->method = function($self){
    echo 'I am a new dynamic method';
   $self->publicMethod(); //есть доступ только к публичным свойствам и методам
};

$b->method->__invoke($b); //вызов через магический метод

$b->method(); //вызов через перехват обращения к методу

//call_user_func($b->{'method'}, $b); //так не работает
```

В принципе можно и переопределять старый метод, однако только в случае если он был определен подобным путем. Не совсем удобно. Поэтому в PHP 5.4 появилось возможность связать замыкание с объектом.  

```
$closure = function(){
	return $this->privateMethod();
}

$closure->bindTo($b,  $b); //второй параметр определяет область видимости
$closure();
```

Конечно, модификации объекта не получилось, тем не менее замыкание получает доступ к приватным функциям и свойствам.  

#### Передача как параметры по умолчанию в методы доступа к данным

Пример получения значения из массива GET. В случае его отсутствия значение будет получено путем вызова функции.  

```
$name = Input::get('name', function() {return 'Fred';});
```

#### Функции высшего порядка

Здесь уже был пример создания валидатора. Приведу пример из фреймворка [lithium](http://lithify.me/)  

```
/**
 * Writes the message to the configured cache adapter.
 *
 * @param string $type
 * @param string $message
 * @return closure Function returning boolean `true` on successful write, `false` otherwise.
 */
public function write($type, $message) {
	$config = $this->_config + $this->_classes;

	return function($self, $params) use ($config) {
		$params += array('timestamp' => strtotime('now'));
		$key = $config['key'];
		$key = is_callable($key) ? $key($params) : String::insert($key, $params);

		$cache = $config['cache'];
		return $cache::write($config['config'], $key, $params['message'], $config['expiry']);
	};
}
```

Метод возвращает замыкание, которое может быть использовано потом для записи сообщения в кеш.  

#### Передача в шаблоны

Иногда в шаблон удобно передавать не просто данные, а, например, сконфигурированную функцию, которую можно вызвать из кода шаблона для получения каких либо значений.  

```
//В контроллере
$layout->setLink = function($setId) use ($userLogin)
{
    return '/users/' . $userLogin . '/set/' . $setId;
};

//В шаблоне
<a href=<?=$this->setLink->__invoke($id);?>>Set name</a>
```

В данном случае в шаблоне генерировалось несколько ссылок на сущности пользователя и в адресах этих ссылок фигурировал его логин.  

#### Рекурсивное определение замыкания

Напоследок о том, как можно задавать рекурсивные замыкания. Для этого нужно передавать в use ссылку на замыкание, и вызывать ее в коде. Не забывайте об условии прекращения рекурсии  

```
$factorial = function( $n ) use ( &$factorial ) {
    if( $n == 1 ) return 1;
    return $factorial( $n - 1 ) * $n;
};

print $factorial( 5 );
```

Многие из примеров выглядят натянуто. Сколько лет жили без них — и ничего. Тем не менее иногда применение замыкания достаточно естественно и для PHP. Умелое использование этой возможности позволит сделать код более читаемым и увеличить эффективность работы программиста. Просто нужно немного подстроить свое мышление под новую парадигму и все станет на свои места. А вообще рекомендую сравнить, как используются такие вещи в других языках типа Python. Надеюсь, что кто-нибудь нашел для себя здесь что-то новое. И конечно, если кто-то знает еще какие-нибудь интересные применения замыканий, то очень жду ваши комментарии. Спасибо!

Теги:
:   * [php](https://habr.com/ru/search/?q=%5Bphp%5D&target_type=posts)
    * [замыкания](https://habr.com/ru/search/?q=%5B%D0%B7%D0%B0%D0%BC%D1%8B%D0%BA%D0%B0%D0%BD%D0%B8%D1%8F%5D&target_type=posts)

    Добавить метки

Укажите причину минуса, чтобы автор поработал над ошибками

Отправить анонимно

Пометьте публикацию своими метками  
 Метки лучше разделять запятой. Например: *программирование, алгоритмы*  

Сохранить

Ой, у вас баннер убежал!  

[Ну. И что?](https://u.tmtm.ru/tmtalkadblock)

[Реклама](https://tmtm.ru/services/advertising/)

* +65
* 501
* 127k
* [51](https://habr.com/ru/post/147620/#comments)
* Поделиться

  + Скопировать ссылку
  + [Facebook](https://www.facebook.com/sharer/sharer.php?u=https://habr.com/ru/post/147620/ "Facebook")
  + [Twitter](https://twitter.com/intent/tweet?text=%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5+%D0%B7%D0%B0%D0%BC%D1%8B%D0%BA%D0%B0%D0%BD%D0%B8%D0%B9+%D0%B2+PHP+https://habr.com/p/147620/+via+%40habr_com "Twitter")
  + [ВКонтакте](https://vk.com/share.php?url=https://habr.com/ru/post/147620/ "ВКонтакте")
  + [Telegram](https://t.me/share/url?url=https://habr.com/ru/post/147620/&title=Применение%20замыканий%20в%20PHP "Telegram")
  + [Pocket](https://getpocket.com/edit?url=https://habr.com/ru/post/147620/&title=Применение%20замыканий%20в%20PHP "Pocket")

Выберите рекомендации для отправки автору:  

Указан только блог     Орфографические ошибки    Пунктуационные ошибки    Отступы    Текст-простыня    Короткие предложения    Смайлики    Много форматирования    Картинки    Ссылки    Оформление кода    Рекламный характер

Отправить

Нарушение  
 Опишите суть нарушения  

Отправить

[![](//habrastorage.org/getpro/habr/avatars/b79/4ae/4bc/b794ae4bcf85f36de7caa65b12c3ccab.png)](https://habr.com/ru/users/neyronius/)    

[neyronius](https://habr.com/ru/users/neyronius/) [neyronius](/users/neyronius/)

Пользователь

Платежная система

## Похожие публикации

* 6 июня 2012 в 11:55  

  **[Наглядный пример использования замыканий в PHP](https://habr.com/ru/post/145317/)**

  +22   10,9k   179   [40](https://habr.com/ru/post/145317#comments "Комментарии")
* 18 января 2012 в 17:06  

  **[Шаблонизация в PHP при помощи лямбда-функций и замыканий](https://habr.com/ru/post/136516/)**

  +5   3,7k   42   [19](https://habr.com/ru/post/136516#comments "Комментарии")
* 10 сентября 2010 в 15:34  

  **[Замыкания в php](https://habr.com/ru/post/103983/)**

  +76   43,6k   178   [69](https://habr.com/ru/post/103983#comments "Комментарии")

## [Вакансии](https://career.habr.com/vacancies)

* [PHP-разработчик (Битрикс/Yii2)	  	  	до 70 000     DigitalWand Можно удаленно](https://career.habr.com/vacancies/1000054132)
* [PHP-разработчик	  	  	от 140 000 до 210 000     ЧИТАЙ-ГОРОД Москва](https://career.habr.com/vacancies/1000055720)
* [Backend разработчик (PHP)	  	  	от 100 000 до 150 000     Modens Group Москва Можно удаленно](https://career.habr.com/vacancies/1000057072)
* [Middle PHP-разработчик	  	  	от 100 000 до 160 000     Spectrum Екатеринбург](https://career.habr.com/vacancies/1000056126)
* [PHP-разработчик	  	  	от 70 000 до 120 000     Директ Кредит Казань](https://career.habr.com/vacancies/1000050828)

[Больше вакансий на Хабр Карьере](https://career.habr.com/vacancies/)

AdBlock похитил этот баннер, но баннеры не зубы — отрастут  

[Подробнее](https://u.tmtm.ru/tmtalkadblock)

[Реклама](https://tmtm.ru/services/advertising/)

## Комментарии 51

* [Rhaps107](https://habr.com/ru/users/Rhaps107/)   12 июля 2012 в 13:23  

  +12

  На PHP 5.3 обратил внимание на такую особенность: переменные, упомянутые в use(), если являлись «ссылками», то перестают ими быть.  

  Например  

  ```
  $contracts  = ...;
  $services = ...;

  foreach ($contracts as &$contract) {

      $contract['xxx'] = 'yyy'; // тут меняется $contracts
      $contractServices = array_filter($services, function($v) use ($contract){
           return $v['id'] == $contract['contractId'];
      });

      $contract['mmm'] = 'nnn'; // а здесь $contract уже живёт своей жизнью, $contracts не меняется

  }
  ```

  Проблему решает амперсенд — use (&$contract), но, имхо, такое поведение оказалось неочевидным.

  + [![](//habrastorage.org/r/w48/getpro/habr/avatars/b79/4ae/4bc/b794ae4bcf85f36de7caa65b12c3ccab.png) neyronius](https://habr.com/ru/users/neyronius/)   12 июля 2012 в 13:37  

    +3

    Да. Поэтому и при рекурсивном определении замыкания в use передается ссылка с амперсандом, несмотря на то, что параметр и так объект и должен передаваться по ссылке. Скорее всего это потому что, use — это не передача параметров в функцию, а разрешение на доступ к переменным родительской области видимости после определения функции. Поэтому по-умолчанию происходит копирование значений, если явно не указана передача по ссылке.

    - [Rhaps107](https://habr.com/ru/users/Rhaps107/)   12 июля 2012 в 14:40  

      +1

      Спасибо. Путает скорее название конструкции — «use», подсознательно предполагаешь, что оно будет использовать имеющиеся инстансы переменных вместо их клонирования :) Мысленно ставлю вам плюс.
  + [![](//habrastorage.org/r/w48/getpro/habr/avatars/2e5/aa9/d97/2e5aa9d97e53370462df02a3e655db98.jpg) ivvi](https://habr.com/ru/users/ivvi/)   12 июля 2012 в 16:26  

    0

    Что-то я не понял смысла в амперсанде вот тут: foreach ($contracts as &$contract)

    - [![](//habrastorage.org/r/w48/getpro/habr/avatars/d28/085/a61/d28085a611874d741f63d3553f1fe0ff.jpg) sectus](https://habr.com/ru/users/sectus/)   12 июля 2012 в 16:30  

      +1

      [Подводный камень в foreach($items as &$item)](http://habrahabr.ru/post/136835/)
  + [![](//habrastorage.org/r/w48/getpro/habr/avatars/d28/085/a61/d28085a611874d741f63d3553f1fe0ff.jpg) sectus](https://habr.com/ru/users/sectus/)   12 июля 2012 в 16:46  

    0

    Если я правильно понял, то это [баг поправили](https://bugs.php.net/bug.php?id=50230) .
  + [![](//habrastorage.org/r/w48/getpro/habr/avatars/1b3/0cc/f7c/1b30ccf7ce4b954ddba12e8377d9751b.jpg) vanxant](https://habr.com/ru/users/vanxant/)   12 июля 2012 в 16:47  

    0

    Вы просто не поняли суть замыканий. Перечисленное в use захватыется с теми значениями, которые оно было на момент вычисления выражения с замыканием.  
    Например для простоты, пусть у вас обычный нумерованный массив каких-то объектов (с индексами 0, 1, 2 и т.п.). На каждый объект вам нужно повесить одинаковый callback или event, но внутри этого callback-а вам нужно знать индекс обрабатываемого объекта в массиве, а взять снаружи скажем неоткуда (ну скажем этот callback вызывается из какой-то библиотеки, которая рассчитана на одиночные объекты и знать не знает про ваши массивы). Вот здесь вы используете как раз замыкания  

    ```
    for($i=0;$i<count($obj_array);++$i) 
        $obj_array[$i].onevent = function () use($i) { /*echo $i...*/}
    ```

    Если бы не было замыкания, вы бы эту $i никак не вытащили.

    - [Fortop](https://habr.com/ru/users/Fortop/)   12 июля 2012 в 19:30  

      0

      Передать ее параметром в само замыкание не судьба?

      * [![](//habrastorage.org/r/w48/getpro/habr/avatars/1b3/0cc/f7c/1b30ccf7ce4b954ddba12e8377d9751b.jpg) vanxant](https://habr.com/ru/users/vanxant/)   12 июля 2012 в 19:48  

        0

        Нет, если этот onevent вызывается какой-то сторонней библиотекой.
* [![](//habrastorage.org/r/w48/getpro/habr/avatars/9fd/804/4bd/9fd8044bd0ea8f7400b3fd56508e2454.jpg) MUTOgen4eg](https://habr.com/ru/users/MUTOgen4eg/)   12 июля 2012 в 13:27  

  0

  По-моему замыкания стоит использовать только в случае, когда очень(!) необходимо сохранить состояние и в обработчиках (не более 5 на событие). Остальное все от лукавого
* [Imenem](https://habr.com/ru/users/Imenem/)   12 июля 2012 в 13:48  

  +6

  Вот вам еще в копилку, из реального проекта, обертка для Doctrine DQL ExpressionBuilder:  

  **Немного магии замыканий**  

  ```
      /**
       * Метод возвращает набор лямбда-функций
       * для удобного доступа к выражениями Doctrine DQL.
       *
       * @example
       *
       * <code>
       *     $query_builder = $this->createSelect();
       *
       *     // импортируем все лямбда-функции в текущую область видимости
       *     extract($this->getExpressions());
       *
       *     $query_builder->where
       *     (
       *          // построим WHERE с помощью лямбда-функций
       *          $andx
       *          (
       *              $eq($alias('user'), ':user'),
       *              $eq($alias('type'), ':type'),
       *              $in($alias('status'), array(':active', ':disabled'))
       *          )
       *     );
       * </code>
       *
       * @return      array
       */
      public function getExpressions()
      {
          if (!empty (static::$expressions))
          {
              return static::$expressions;
          }

          $expr_builder = $this->getExpressionBuilder();

          // :TRICKY:         Imenem          22.03.12
          //
          // Эта лямбда-функция создает прокси
          // к методу объекта ExpressionsBuilder.
          // После ее вызова с указанием имени метода
          // будет создана лямбда-функция,
          // которая вызывает одноименный метод ExpressionsBuilder,
          // передавая ему полученные параметры.
          $expr_proxy = function($method) use ($expr_builder)
          {
              return function() use ($method, $expr_builder)
              {
                  return call_user_func_array(array($expr_builder, $method), func_get_args());
              };
          };

          $alias  = static::$alias;

          static::$expressions = array
          (
              'alias' => function($field) use ($alias)
              {
                  return $alias . '.' . $field;
              },
              'andx'      => $expr_proxy('andx'),
              'orx'       => $expr_proxy('orx'),
              'eq'        => $expr_proxy('eq'),
              'neq'       => $expr_proxy('neq'),
              'gte'       => $expr_proxy('gte'),
              'lte'       => $expr_proxy('lte'),
              'in'        => $expr_proxy('in'),
              'notIn'     => $expr_proxy('notIn'),
              'between'   => $expr_proxy('between'),
              'not'       => $expr_proxy('not'),
              'exists'    => $expr_proxy('exists')
          );

          return static::$expressions;
      }
  ```

  **Пример DQL-запроса**  

  ```
      /**
       * Метод возвращает актуальные на текущий день
       * запланированные платежи по уровню баланса
       *
       * @param       DateTime        $date           Метка времени запуска
       * @param       int             $offset         Индекс первого элемента, который должен попасть в выборку
       * @param       int             $limit          Максимальное кол-во элементов в выборке
       *
       * @return      Acme\SomeBundle\Entity\ScheduleItem[]              Массив запланированных задач
       */
      public function findActualBalanceSchedules(DateTime $date = null, $offset = null, $limit = null)
      {
          extract($this->getExpressions());

          $pt_repo = $this->getRepo('PaymentTask');

          // получим лямбду, которая добавляет
          // алиас сущности PaymentTask к имени поля
          $pt_alias = $pt_repo->getExpressions()['alias'];

          // создадим подзапрос, который выберет
          // для каждой ScheduleItem все PaymentTask,
          // которые были созданы не позднее суток назад,
          // и не были до конца выполнены
          $created_payment_tasks = $pt_repo
              ->createSelect()
              ->select($pt_alias('id'))
              ->andWhere
              (
                  $gte($pt_alias('started'), ':started'),
                  $in($pt_alias('status'),   PaymentTask::getActiveStatusSet())
              );

          return $this
              ->createActualSelect(ScheduleItem::TYPE_BALANCE, $offset, $limit)
              ->andWhere
              (
                  // выберем все запланированные задачи по балансу,
                  // для которых не существует неоконченных платежных задач
                  $not($exists($created_payment_tasks))
              )
              // выберем задачи, созданные не позднее суток назад
              ->setParameter('started', (new DateTime)->sub(new DateInterval('P1D')))
              ->getQuery()
              ->getResult();
      }
  ```
* [VolCh](https://habr.com/ru/users/VolCh/)   12 июля 2012 в 14:20  

  +1

  *Как видим, замыкание как и лямбда-функция представляют собой объект класса Closure*  

  Стоит уточнить, наверное, что лямбда-функция это частный случай замыкания.  

  А использование замыканий в PHP отчасти непопулярно, по-моему, из-за специфики PHP, работающего в CGI-режиме (логически). Грубо говоря нет никакой разницы писать function ($request\_param, $config\_param) или function ($request\_param) use ($config\_param), если $config\_param вычисляется при каждом запросе так же как $request\_param.
* [![](//habrastorage.org/r/w48/getpro/habr/avatars/201/907/050/2019070505b75896c2f6010fb563b2e3.png) Twin](https://habr.com/ru/users/Twin/)   12 июля 2012 в 14:36  

  0

  Примеры кода на PHP это классно, но по-моему большинство идей использования можно почерпнуть из [en.wikipedia.org/wiki/Closure\_](http://en.wikipedia.org/wiki/Closure_) (computer\_science)
* [![](//habrastorage.org/r/w48/getpro/habr/avatars/735/521/f5b/735521f5bbfb5f2a8333f07ea2f1dce9.jpg) WoZ](https://habr.com/ru/users/WoZ/)   12 июля 2012 в 14:40  

  +2

  Я вот не вижу преимуществ использования замыканий. Почти все можно реализовать без их использования, но используя их, код становится сложнее и менее понятным, его сложнее поддерживать и развивать. В определенный момент поддержка такого кода может отнять времени больше чем было сэкономлено при написании кода с использованием замыканий.

  + [Imenem](https://habr.com/ru/users/Imenem/)   12 июля 2012 в 15:09  

    0

    У замыканий есть такое преимущество, как возможность легковесного хранения состояния. Рассмотрим пример в котором имеются:  
    1. Порционный итератор (получает абстрактный загрузчик данных, передает ему границы порции и получает в ответ данные)  
    2. Репозиторий сущностей, который не хранит состояние и его метод для получения данных, который требует множество параметров, кроме возможных границ порции.  
    3. Сервис, который использует доступ к репозиторию с помощью порционного итератора, который тоже не хранит состояние  

    Используя замыкание мы можем создать легковесный адаптер, не внося изменений в репозиторий, итератор или сервис:  

    ```
        public function getActualScheduleItems(DateTime $date = null, DateTimeZone $time_zone = null)
        {
            $data_loader = function($offset, $limit) use ($date, $time_zone)
            {
                return $this->getRepo()->findActualPeriodicalSchedules($date, $time_zone, $offset, $limit);
            };

            return $this->createPortionIterator($data_loader);
        }
    ```

    - [![](//habrastorage.org/r/w48/getpro/habr/avatars/735/521/f5b/735521f5bbfb5f2a8333f07ea2f1dce9.jpg) WoZ](https://habr.com/ru/users/WoZ/)   12 июля 2012 в 15:26  

      0

      Понятное дело что удобнее, я этого не отрицал. Согласитесь, можно этот код написать и не используя замыкания. Я писал о том, что замыкания усложняют отладку и поддержку кода. А если неаккуратно ними пользоваться, то может еще и память течь.

      * [Imenem](https://habr.com/ru/users/Imenem/)   12 июля 2012 в 15:55  

        0

        Тогда подкрепите свои слова примером того, как можно переписать это без замыканий, не сохраняя состояние в сервисе или репозитории (это идеологически и архитектурно неправильно). Я вот утверждаю, что некоторые куски кода короче, элегантнее и понятнее (выберите любые два :) с использованием замыканий.

        + [![](//habrastorage.org/r/w48/getpro/habr/avatars/735/521/f5b/735521f5bbfb5f2a8333f07ea2f1dce9.jpg) WoZ](https://habr.com/ru/users/WoZ/)   12 июля 2012 в 16:24  

          0

          Просто взять и переписать, сохранив логику примера выше, красиво не выйдет. Весь дизайн кода будет отличаться, вот в примере предполагается сохранение состояние. Изменив дизайн, его можно сохранять в полях класса. Можно передавать постоянно аргументами, можно просто оформить в виде класса. Я не говорю что все сказанное применимо к этому примеру, замечу еще раз, если проектировать не предполагая использование замыканий, то задачу можно решить и без них. Просто иной подход будет.

          - [Imenem](https://habr.com/ru/users/Imenem/)   12 июля 2012 в 16:52  

            0

            Сервисы и репозитории в принципе не могут хранить состояние, поэтому в полях класса хранить его нельзя. Оформить в виде класса то, что можно оформить в виде замыкания — громоздко и вряд-ли более понятно. Куча мелких классов-адаптеров — куча мелких файлов в ФС. Передавать аргументами — требует идентичности интерфейсов, а соответственно изменения классов или наследования.  

            > если проектировать не предполагая использование замыканий, то задачу можно решить и без них

            Да, вот только зачем отвергать решения, которые позволяют решить задачу лучше и проще? Здесь как раз замыкания вполне соответствуют KISS. В любой точке, в которой возможна передача коллбэка, можно, а зачастую и нужно, использовать замыкание, чтобы не плодить методы/наследники-адаптеры.
    - [![](//habrastorage.org/r/w48/getpro/habr/avatars/655/565/474/655565474e32f20d2c545609396f22e7.jpg) gen](https://habr.com/ru/users/gen/)   12 июля 2012 в 15:34  

      +1

      Стоит, наверное, уточнить, что этот пример будет работать только с версии 5.4 из-за указателя $this внутри замыкания.

      * [Imenem](https://habr.com/ru/users/Imenem/)   12 июля 2012 в 15:40  

        0

        Любой, кто знает PHP сможет переписать пример так, чтобы он работал в 5.3:  

        ```
            public function getActualScheduleItems(DateTime $date = null, DateTimeZone $time_zone = null)
            {
                $repo = $this->getRepo();

                $data_loader = function($offset, $limit) use ($repo, $date, $time_zone)
                {
                    return $repo->findActualPeriodicalSchedules($date, $time_zone, $offset, $limit);
                };

                return $this->createPortionIterator($data_loader);
            }
        ```

        + [![](//habrastorage.org/r/w48/getpro/habr/avatars/655/565/474/655565474e32f20d2c545609396f22e7.jpg) gen](https://habr.com/ru/users/gen/)   12 июля 2012 в 15:58  

          0

          Несомненно, я лишь хотел съэкономить немного времени тем, кто только разбирается с замыканиями и не знает про ньюанс с $this, тем более, что в статье про это ничего не сказано.
  + [tnz](https://habr.com/ru/users/tnz/)   12 июля 2012 в 15:19  

    +1

    Очень удобно передавать callback во всякие array\_filter. Бывает удобно передать функцию куда-то внутрь.
* [![](//habrastorage.org/r/w48/getpro/habr/avatars/375/007/8ec/3750078ecc29e4bd60070a9d28cfecb4.png) Stdit](https://habr.com/ru/users/Stdit/)   12 июля 2012 в 15:39  

  +2

  Замыкания прекрасны, пусть и не настолько удобны и лаконичны, как в ECMAScript. Главное использовать их с умом и только тем, где это действительно удобно и нужно, а не потому что «это круто, модно, современно». А то есть риск получить неизлечимую злокачественную опухоль.
* [![](//habrastorage.org/r/w48/getpro/habr/avatars/49d/5f3/632/49d5f36329bdf6ad46f2753c431e8adb.png) alpust](https://habr.com/ru/users/alpust/)   12 июля 2012 в 15:48  

  0

  ```
  $expr
  ->if(function(){ return $this->v == 4;})
  ->then(function(){$this->v = 42;})
  ->else(function(){})
      ->elseif(function(){})
  ->end()
  ->while(function(){$this->v >=42})
      ->do(function(){
          $this->v --;
  })
  ->end()
  ```

  ИМХО попахивает Монадами.
* [![](//habrastorage.org/r/w48/getpro/habr/avatars/b8f/2bb/403/b8f2bb4033ed79dfd157249241cc323c.jpg) Epsiloncool](https://habr.com/ru/users/Epsiloncool/)   12 июля 2012 в 15:56  

  –1

  Крайний с конца пример как бы намекает нам на возможность развития функционального программирования в PHP.

  + [tnz](https://habr.com/ru/users/tnz/)   13 июля 2012 в 01:48  

    0

    Вот как раз топик по теме [habrahabr.ru/post/147612/](http://habrahabr.ru/post/147612/)

    - [![](//habrastorage.org/r/w48/getpro/habr/avatars/b8f/2bb/403/b8f2bb4033ed79dfd157249241cc323c.jpg) Epsiloncool](https://habr.com/ru/users/Epsiloncool/)   13 июля 2012 в 02:31  

      0

      Вообще-то я про другое имел ввиду ))
* [![](//habrastorage.org/r/w48/getpro/habr/avatars/3e4/61a/a27/3e461aa27e5775909756710c697ce0ae.jpg) taliban](https://habr.com/ru/users/taliban/)   12 июля 2012 в 16:41  

  +4

  «замыкание как и лямбда-функция представляют собой объект класса Closure»  
  Автор, вы уж почитайте до конца что такое лямбда функция и что такое замыкание. Лямбда функция — это то что вы называете замыканием, и именно она есть обтект класса Closure, а замыкание это действие при котором этот обьект помнит что находилось вокруг него при создании (именно кусочек который прячется за оператором use).

  + [![](//habrastorage.org/r/w48/getpro/habr/avatars/b79/4ae/4bc/b794ae4bcf85f36de7caa65b12c3ccab.png) neyronius](https://habr.com/ru/users/neyronius/)   12 июля 2012 в 16:49  

    0

    Спасибо за уточнение. Вы правы.
* [![](//habrastorage.org/r/w48/getpro/habr/avatars/2f0/e8d/46a/2f0e8d46a0790046ad3a85aaf315b4ea.jpg) LisTik](https://habr.com/ru/users/LisTik/)   12 июля 2012 в 16:44  

  0

  Валидация — 1-й пример:  
  …  
  return frunction($v) use ($min, $max){  
  …  

  В слове frunction — ошибка

  + [![](//habrastorage.org/r/w48/getpro/habr/avatars/b79/4ae/4bc/b794ae4bcf85f36de7caa65b12c3ccab.png) neyronius](https://habr.com/ru/users/neyronius/)   12 июля 2012 в 16:50  

    0

    Спасибо, исправил
  + [![](//habrastorage.org/r/w48/getpro/habr/avatars/2f0/e8d/46a/2f0e8d46a0790046ad3a85aaf315b4ea.jpg) LisTik](https://habr.com/ru/users/LisTik/)   12 июля 2012 в 17:17  

    0

    А минус-то за что? Странно…
* [![](//habrastorage.org/r/w48/getpro/habr/avatars/1b3/0cc/f7c/1b30ccf7ce4b954ddba12e8377d9751b.jpg) vanxant](https://habr.com/ru/users/vanxant/)   12 июля 2012 в 17:02  

  +1

  Замыкания — элегантный способ делать Dependancy Injection. См. например, прекрасный мини-фреймворк [Silex](http://silex.sensiolabs.org/documentation) .  
  Предположим, у вас есть некий интерфейс (скажем той же callback функции), который вы менять не хотите или не можете.  
  Но вам в каком-то месте потребовалось сделать функцию с этим интерфейсом, которой нужно зачем-то лезть в базу данных.  
  Откуда эта функция возьмет объект соединения с БД?  
  До PHP 5.3. практически единственным способом было объявить глобальную переменную global $db, или ну или global $app; $db = $app->db;  
  Но это засоряет глобальную область видимости и не очень работает, если у вас несколько соединений с дб.  
  С замыканиями вы просто объявляете функцию с нужным интерфейсом и передаете ей линк на $db через use ($db) в момент объявления.
* [![](//habrastorage.org/r/w48/getpro/habr/avatars/f7d/520/7d4/f7d5207d45996e1c7f74df7019dcbbba.png) vovs](https://habr.com/ru/users/vovs/)   12 июля 2012 в 17:06  

  –2

  Простите, я вот понять не могу этих нововведений. PHP != Javascript. Он не событийный язык. Я не могу понять, зачем из танка самолет делать?

  + [![](//habrastorage.org/r/w48/getpro/habr/avatars/b79/4ae/4bc/b794ae4bcf85f36de7caa65b12c3ccab.png) neyronius](https://habr.com/ru/users/neyronius/)   12 июля 2012 в 17:08  

    +1

    Лямбда функции не только в JS используются и не только для событий.
  + [![](//habrastorage.org/r/w48/getpro/habr/avatars/b20/891/a5b/b20891a5b6e6d7f973bcb454472fd187.gif) dxArtem](https://habr.com/ru/users/dxArtem/)   12 июля 2012 в 17:28  

    0

    переменная = функция, use и т.д. есть и в С++11x
  + [![](//habrastorage.org/r/w48/getpro/habr/avatars/1b3/0cc/f7c/1b30ccf7ce4b954ddba12e8377d9751b.jpg) vanxant](https://habr.com/ru/users/vanxant/)   12 июля 2012 в 20:11  

    0

    Замыкания редко вот прям чтоб необходимы, но во многих случаях просто удобны своим простым синтаксисом.  
    Ну как пример — таблица футбольного чемпионата, нужно сделать сортировку, кто какое место занял по заданной турнирной таблице (там трюки при равенствен очков), при этом очень хочется использовать стандартный алгоритм uasort (ну не писать же свой пузырёк в тысячный раз, правильно).  
    Попробуйте сделать это с замыканиями и без — поймете разницу.
  + [![](//habrastorage.org/r/w48/getpro/habr/avatars/b8f/2bb/403/b8f2bb4033ed79dfd157249241cc323c.jpg) Epsiloncool](https://habr.com/ru/users/Epsiloncool/)   13 июля 2012 в 18:41  

    +1

    Вы очень сильно ошибаетесь насчёт «PHP это не событийный язык». Костыли по поводу внедрения событий в PHP встречаются ещё со времён первой версии Pear'а, а сейчас это имеет массовый характер. Если во фреймворке нет поддержки событий (хуков), то он плох. Сейчас наступают времена асинхронности, а там без событий ну никак нельзя, поэтому готовьтесь. Читайте мануал по phpDaemon и привыкайте к событийности ))

    - [![](//habrastorage.org/r/w48/getpro/habr/avatars/f7d/520/7d4/f7d5207d45996e1c7f74df7019dcbbba.png) vovs](https://habr.com/ru/users/vovs/)   13 июля 2012 в 19:09  

      0

      Я, коллега, все прекрасно понимаю, и понимаю куда все движется. И готовлюсь — изучаю Node.js  
      И лично я считаю что в PHP это все и останется костылями, ибо чтобы это все \_действительно\_ работало, нужна другая идеология построения, как протокола, так и веб сервера, так и протокола http. И для человека, который хоть как то работал с javascript, все эти нововведения в PHP, ну ни как новыми не кажутся :-)

      * [![](//habrastorage.org/r/w48/getpro/habr/avatars/b8f/2bb/403/b8f2bb4033ed79dfd157249241cc323c.jpg) Epsiloncool](https://habr.com/ru/users/Epsiloncool/)   13 июля 2012 в 19:17  

        0

        Ну а как же phpDaemon? Активно развивается. И хотя мне кажется, что nodejs местами попроще, в phpd есть свой скрытый смысл, преимущества над nodejs. Там кстати тоже уже есть и WS-клиенты и всякие XMPP-протоколы поддерживаются.

        + [![](//habrastorage.org/r/w48/getpro/habr/avatars/f7d/520/7d4/f7d5207d45996e1c7f74df7019dcbbba.png) vovs](https://habr.com/ru/users/vovs/)   13 июля 2012 в 19:44  

          0

          По мне, это костыль. Ну для того, чтобы это все действительно работало, нужно другой, абсолютно другой подход ко всей клиент-серверной структуре. Node.js — это и веб-сервер и язык программирование, все вместе. Именно это дает такую чудовищную мощность и гибкость. Linux + Apach + MySQL + PHP !== node.js. Я даже не знаю как выразиться точней, ибо я не могу языком PHP выразить то, что выражаю nodejs, и появление таких конструкций, как [] и {} в PHP 5.4, а также, замыканий, анонимных функций, глазами человека, который практикует javascript + nodejs выглядит… ну просто обескураживающей. Ну это просто мысли в слух, ни ради холивара. Мне очень нравится PHP, очень, и он действительно проще, чем javascript, и в первую очередь, на мой взгляд, благодаря синхронному выполнению и отсутствия событий, анонимных функций, замыканий и т.д.

          - [![](//habrastorage.org/r/w48/getpro/habr/avatars/b8f/2bb/403/b8f2bb4033ed79dfd157249241cc323c.jpg) Epsiloncool](https://habr.com/ru/users/Epsiloncool/)   13 июля 2012 в 19:55  

            +1

            Вы смотрели phpd? Там нет никаких Apache, он сам себе сервер. По сути это то же самое, что и nodejs, только на php. Без linux и mysql вы не обойдётесь, они сами по себе, отдельно.  
            К сожалению, того PHP, которого мы знали 5 лет назад, скоро уже не будет. Всё будет асинхронно и персистентно)
* [![](//habrastorage.org/r/w48/getpro/habr/avatars/3d0/c39/b5f/3d0c39b5fa2d743b09f4592017996389.jpg) kuzemchik](https://habr.com/ru/users/kuzemchik/)   13 июля 2012 в 07:22  

  0

  Наконецто можно нормально использовать array\_map и прочее. Писать имена функций определенных рядом строкой, ну совсем неприятно было.

  + [![](//habrastorage.org/r/w48/getpro/habr/avatars/3d0/c39/b5f/3d0c39b5fa2d743b09f4592017996389.jpg) kuzemchik](https://habr.com/ru/users/kuzemchik/)   13 июля 2012 в 07:55  

    +1

    :%s/наконецто/наконец-то/g
  + [zim32](https://habr.com/ru/users/zim32/)   15 июля 2012 в 23:37  

    0

    //Time: 0.4395  
    //Time: 0.0764  
    А мне это уже не кажется хорошей идеей

    - [![](//habrastorage.org/r/w48/getpro/habr/avatars/3d0/c39/b5f/3d0c39b5fa2d743b09f4592017996389.jpg) kuzemchik](https://habr.com/ru/users/kuzemchik/)   20 июля 2012 в 10:49  

      0

      Не знаю что за цифры вы привели. У меня таких отличий в производительности не наблюдается.  

      test1.php  

      ```
      <?php
      $array = range(0, 100000);
      $result = array_map(function($element) { return $element+1; },$array);
      ```

      test2.php  

      ```
      <?php
      $array = range(0, 100000);
      function test($element) { return $element+1;}
      array_map('test',$array);
      ```

      * [![](//habrastorage.org/r/w48/getpro/habr/avatars/b79/4ae/4bc/b794ae4bcf85f36de7caa65b12c3ccab.png) neyronius](https://habr.com/ru/users/neyronius/)   20 июля 2012 в 10:52  

        0

        Разница не между способом вызова анонимной функции, а между обработкой каждого элемента данных с помощью анонимной функции и обычной итерацией массива.

        + [![](//habrastorage.org/r/w48/getpro/habr/avatars/3d0/c39/b5f/3d0c39b5fa2d743b09f4592017996389.jpg) kuzemchik](https://habr.com/ru/users/kuzemchik/)   20 июля 2012 в 10:59  

          0

          Ясно, исходил из темы топика.
* [DjOnline](https://habr.com/ru/users/DjOnline/)   23 июля 2012 в 10:37  

  +1

  >>$name = Input::get('name', function() {return 'Fred';});  
  Вот зачем изобретать велосипед, если и короче и понятнее можно написать  
  $name=isset($\_GET['name'])?$\_GET['name'] :'Fred');

  + [![](//habrastorage.org/r/w48/getpro/habr/avatars/d28/085/a61/d28085a611874d741f63d3553f1fe0ff.jpg) sectus](https://habr.com/ru/users/sectus/)   23 июля 2012 в 11:37  

    0

    Пример может быть более сложным, например, значение по умолчанию нужно брать из базы.  

    ```
    $name = Input::get('name', function() use ($db){$config = $db->loadConfig(); return $config['default_name'];});
    ```

    В Вашем же случае либо придётся написать дополнительное условие  

    ```
    $name=isset($_GET['name'])?$_GET['name'] :null); 
    if (is_null($name))
      {
      $config = $db->loadConfig(); 
      $name = $config['default_name'];
      }
    ```

    , либо при каждом запросе обращаться к базе.  

    ```
    $config = $db->loadConfig(); 
    $default_name = $config['default_name'];
    $name=isset($_GET['name'])?$_GET['name'] :$default_name); 
    ```

Только [полноправные пользователи](/info/help/registration/) могут оставлять комментарии. [Войдите](https://habr.com/ru/auth/login/) , пожалуйста.

### Что обсуждают

* [Сейчас](#broadcast_comments_now)
* [Вчера](#broadcast_comments_yesterday)
* [Неделя](#broadcast_comments_week)

* [IPv6 — прекрасный мир, стоящий скорого перехода на него](https://habr.com/ru/post/490378/)  

  12,2k   [291](https://habr.com/ru/post/490378/#comments)
* [Самодельный автопилот на одноплатном компьютере (SBC) Tinker board и Arduino DUE](https://habr.com/ru/post/490572/)  

  8,4k   [36](https://habr.com/ru/post/490572/#comments)
* [Выпуск#31: ITренировка — актуальные вопросы и задачи от ведущих компаний](https://habr.com/ru/company/spice/blog/489302/)  

  2,5k   [21](https://habr.com/ru/company/spice/blog/489302/#comments)
* [SpaceX провела испытание прототипа Starship SN1, которое закончилось взрывом](https://habr.com/ru/news/t/490506/)  

  17,7k   [141](https://habr.com/ru/news/t/490506/#comments)
* [Корректирующие коды «на пальцах»](https://habr.com/ru/post/328202/)  

  34,4k   [20](https://habr.com/ru/post/328202/#comments)

* [Самодельная подводная лодка с надводной wi-fi антенной](https://habr.com/ru/post/490588/)  

  22,1k   [103](https://habr.com/ru/post/490588/#comments)
* [Домашний кинотеатр на Raspberry](https://habr.com/ru/post/490540/)  

  23,8k   [76](https://habr.com/ru/post/490540/#comments)
* [Когда я слышу слова «нейросеть восстановила», я лезу проверять бэкапы](https://habr.com/ru/post/490620/)  

  20,1k   [75](https://habr.com/ru/post/490620/#comments)
* [Самодельный автопилот на одноплатном компьютере (SBC) Tinker board и Arduino DUE](https://habr.com/ru/post/490572/)  

  8,4k   [36](https://habr.com/ru/post/490572/#comments)
* [Монады как паттерн переиспользования кода](https://habr.com/ru/post/490112/)  

  3,8k   [27](https://habr.com/ru/post/490112/#comments)

* [Полная домашняя автоматизация в новостройке](https://habr.com/ru/post/489610/)  

  97,6k   [410](https://habr.com/ru/post/489610/#comments)
* [FreeBSD: гораздо лучше GNU/Linux](https://habr.com/ru/post/490408/)  

  42,1k   [291](https://habr.com/ru/post/490408/#comments)
* [IPv6 — прекрасный мир, стоящий скорого перехода на него](https://habr.com/ru/post/490378/)  

  12,2k   [291](https://habr.com/ru/post/490378/#comments)
* [Как восстановить светодиодную лампу за 2 минуты при минимальных навыках работы с паяльником и знаниях об электронике](https://habr.com/ru/post/489710/)  

  87,5k   [284](https://habr.com/ru/post/489710/#comments)
* [Обязательно ли высшее образование в IT?](https://habr.com/ru/company/southbridge/blog/489628/)  

  28,2k   [282](https://habr.com/ru/company/southbridge/blog/489628/#comments)

## Самое читаемое

* [Сутки](#broadcast_posts_today)
* [Неделя](#broadcast_posts_week)
* [Месяц](#broadcast_posts_month)

* [В «Яндекс.Такси» начали вычислять социальный рейтинг пассажиров](https://habr.com/ru/news/t/490556/)  

  +18   30,2k   18   [254](https://habr.com/ru/news/t/490556/#comments "Комментарии")
* [Самодельная подводная лодка с надводной wi-fi антенной](https://habr.com/ru/post/490588/)  

  +78   22,1k   138   [103](https://habr.com/ru/post/490588/#comments "Комментарии")
* [Домашний кинотеатр на Raspberry](https://habr.com/ru/post/490540/)  

  +10   23,8k   196   [76](https://habr.com/ru/post/490540/#comments "Комментарии")
* [Когда я слышу слова «нейросеть восстановила», я лезу проверять бэкапы](https://habr.com/ru/post/490620/)  

  +128   20,1k   69   [75](https://habr.com/ru/post/490620/#comments "Комментарии")
* [Тайна длиною в полвека: весь мир на ладони ЦРУ](https://habr.com/ru/company/ua-hosting/blog/490538/)  

  +6   19,6k   70   [12](https://habr.com/ru/company/ua-hosting/blog/490538/#comments "Комментарии")

* [Полная домашняя автоматизация в новостройке](https://habr.com/ru/post/489610/)  

  +118   97,6k   671   [410](https://habr.com/ru/post/489610/#comments "Комментарии")
* [Как восстановить светодиодную лампу за 2 минуты при минимальных навыках работы с паяльником и знаниях об электронике](https://habr.com/ru/post/489710/)  

  +28   87,5k   153   [284](https://habr.com/ru/post/489710/#comments "Комментарии")
* [Собеседование в луже крови](https://habr.com/ru/post/490294/)  

  +178   71,7k   141   [218](https://habr.com/ru/post/490294/#comments "Комментарии")
* [Загружаем и храним в Google Drive файлы любого размера бесплатно. Баг или Фича?](https://habr.com/ru/post/489514/)  

  +132   59,4k   138   [108](https://habr.com/ru/post/489514/#comments "Комментарии")
* [Google Interviewing Process for Software Developer Role in 2020](https://habr.com/ru/post/489698/)  

  +67   57,1k   9   [6](https://habr.com/ru/post/489698/#comments "Комментарии")

* [Samsung удалённо блокирует свои «серые» Smart TV в России. UPD — заявление Samsung](https://habr.com/ru/post/487290/)  

  +150   145k   75   [660](https://habr.com/ru/post/487290/#comments "Комментарии")
* [Коронавирус 2019-nCoV: смертность небольшая, большая летальность](https://habr.com/ru/post/486874/)  

  +143   123k   99   [411](https://habr.com/ru/post/486874/#comments "Комментарии")
* [Мне 14, и я совмещаю школу с работой в ИТ](https://habr.com/ru/company/skyeng/blog/487764/)  

  +279   114k   296   [319](https://habr.com/ru/company/skyeng/blog/487764/#comments "Комментарии")
* [Заметки о жизни в США](https://habr.com/ru/post/487230/)  

  +276   101k   356   [1203](https://habr.com/ru/post/487230/#comments "Комментарии")
* [Полная домашняя автоматизация в новостройке](https://habr.com/ru/post/489610/)  

  +118   97,6k   671   [410](https://habr.com/ru/post/489610/#comments "Комментарии")

## Рекомендуем

[Разместить](https://tmtm.ru/megapost)

* [![](https://habrastorage.org/getpro/tmtm/pictures/08a/6ce/f72/08a6cef72be80fbbe826d59551d0ef82.jpg)  	Интересно](https://u.tmtm.ru/automate)   [**Как полностью автоматизировать квартиру — реальная история разработчика**](https://u.tmtm.ru/automate)
* [![](https://habrastorage.org/getpro/tmtm/pictures/523/271/143/523271143447b38ac8d0abd843a57c19.jpg)  	Мегапост](https://u.tmtm.ru/p-k-p-270220)   [**Боли сисадмина и как их лечить**](https://u.tmtm.ru/p-k-p-270220)

### Ваш аккаунт

* [Войти](https://habr.com/ru/auth/login/)
* [Регистрация](https://habr.com/ru/auth/register/)

### Разделы

* [Публикации](https://habr.com/ru/posts/top/)
* [Новости](https://habr.com/ru/news/)
* [Хабы](https://habr.com/ru/hubs/)
* [Компании](https://habr.com/ru/companies/)
* [Пользователи](https://habr.com/ru/users/)
* [Песочница](https://habr.com/ru/sandbox/)

### Информация

* [Правила](https://habr.com/ru/info/help/rules/)
* [Помощь](https://habr.com/ru/info/help/)
* [Документация](https://habr.com/ru/info/topics/madskillz/)
* [Соглашение](https://account.habr.com/info/agreement/?hl=ru_RU)
* [Конфиденциальность](https://account.habr.com/info/confidential/?hl=ru_RU)

### Услуги

* [Реклама](https://tmtm.ru/services/advertising/)
* [Тарифы](https://tmtm.ru/services/corpblog/)
* [Контент](https://tmtm.ru/services/content/)
* [Семинары](https://tmtm.ru/workshops/)
* [Мегапроекты](https://habr.com/ru/megaprojects/)

Если нашли опечатку в посте, выделите ее и нажмите Ctrl+Enter, чтобы сообщить автору.

© 2006 – 2020 « [TM](https://tmtm.ru/) »

[Настройка языка](#)

[О сайте](https://habr.com/ru/about/)

[Служба поддержки](https://habr.com/ru/feedback/)

[Мобильная версия](https://m.habr.com/post/147620/?mobile=yes)

Настройка языка

Интерфейс  

Русский

English

Язык публикаций  

Русский

Английский

Сохранить настройки

![](https://www.facebook.com/tr?id=317458588730613&ev=PageView&noscript=1) ![](https://vk.com/rtrg?p=VK-RTRG-421343-57vKE)