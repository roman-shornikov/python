
import telebot
import random
def start(m, res=False):
 @bot.message_handler(content_types=["text"])
 def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
# Создаем экземпляр бота
bot = telebot.TeleBot('5758930042:AAFghEqZlG9iXybJrcPzJ6Zv-xYz0dnle18')
# Список цитат, из которого будут генерироваться цвета
cs=['Если твоя рука в моей руке, я чувствую, что счастлив.', 'До сих пор ищешь во мне кого-то.', 'Минуты ведь были прекрасными.'
    , 'Влюбись в меня так, чтобы унесло.', 'Не надо быть правильным, надо быть настоящим…', 'Самый дешевый товар в мире — это мнение других о тебе.'
    , 'Неважно, сколько ты знаком с человеком. Главное, кем он для тебя стал', 'Цените каждый миг, прожитый со своими родителями.'
    , 'Всё, что ни происходит, всегда так, как нужно, и только к лучшему.', 'Свою жизнь нужно устраивать до тех пор, пока жизнь не начнёт устраивать тебя.'
    , 'Тяжело быть женщиной! Постоянно хочется чего-нибудь купить, кого-нибудь прибить, похудеть и пироженку!'
    , 'Я тоже свалился в мечту, как в море.И меня унесло волной.'
    , 'Если вам кажется, что я слишком многое себе позволяю, возможно, вы просто слишком во многом себе отказываете.', 'Ничего в этой жизни не дается легко. '
    , ' Чтобы достичь своих целей необходимо идти на определенные жертвы — тратить свои силы, время, ограничивать себя в чем-либо'
    , 'Иногда бывают моменты, когда хочется все бросить и отказаться от мечты.'
    , 'В такие моменты вспомните, как много вы получите, если пойдете дальше и как много потеряете, если сдадитесь.'
    , 'Цена успеха, как правило, меньше, чем цена неудачи.', 'Не стоит принимать доброту за слабость, грубость за силу, а подлость за умение жить '
    , 'Берегите в себе человека.', 'Навсегда ничего не бывает.'
    , 'Когда тебя предали, а ты, не смотря ни на что, хочешь общаться с этим человеком и желаешь ему только счастья, то ты или святой или дурак.'
    , 'Ты когда-нибудь чувствовал, что тебе не хватает того, кого ты никогда не встречал?', 'Падает тот, кто бежит. Тот, кто ползет, не падает.'
    , 'Люди могут забыть, что вы сказали. Могут забыть, что вы сделали. Но никогда не забудут, что вы заставили их почувствовать..'
    , 'Люди делятся на две половины. Одни, войдя в комнату, восклицают: "О, кого я вижу!"; другие: "А вот и я!".', 'Красота в глазах смотрящего.'
    , 'Одна из самых серьёзных потерь — потеря времени.', 'Чтобы было легко потом, нужно пройти через трудности сейчас.'
    , 'За сладкое приходится горько расплачиваться.'
    , 'Какая разница, кто сильнее, кто умнее, кто красивее, кто богаче? Ведь, в конечном итоге, имеет значение только то, счастливый ли ты человек или нет.'
    , 'В ожидании крепчает характер, слабеет надежда и умирает любовь…', 'Люби тех, кто любит тебя.'
    , 'Тысячи свечей можно зажечь от одной единственной свечи, и жизнь ее не станет короче. Счастья не становится меньше, когда им делишься.'
    , 'Cпокойствие — сильнее эмоций. Молчание — громче крика. Равнодушие — страшнее войны.'
    , 'Почему мы закрываем глаза, когда молимся, мечтаем или целуемся? Потому что самые прекрасные вещи в жизни мы не видим, а чувствуем сердцем…'
    , 'Время утекает сквозь пальцы опущенных рук.', 'Самая большая ошибка — это боязнь совершить ошибку.'
    , 'Существует право, по которому мы можем отнять у человека жизнь, но нет права, по которому мы могли бы отнять у него смерть.'
    , 'Мы знаем, кто мы есть, но не знаем, кем мы можем быть.', 'Верная любовь помогает переносить все тяготы.'
    , 'Тот, кто назвал женщин прекрасным полом, хотел, быть может, сказать этим нечто лестное для них, но на самом деле выразил нечто большее.'
    ,'Юмор с трудом поддается определению, ведь только отсутствием юмора можно объяснить попытки определить его.'
    , 'Всегда быть правым, всегда идти напролом, ни в чем не сомневаясь, — именно с помощью этих качеств тупость управляет миром.'
    , 'Тот, кто мало знает свет, готов преклонять перед ним колени и обожать его; кто же знает его хорошо, тот больше всего презирает его.'
    , 'Атлас не смог бы удержать мир, если бы задумался о его размерах.']
csreturn=[]
for item in cs:
    csreturn.append(item)
# Строка для записи рандомной цитаты
str = ''

#Строка для записи цитат от пользователя
item = ''

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'СПИСОК КОМАНД: \n\n *Список* \n *Рандом* \n *Добавить*\n *Удалить*\n\n\n\nАВТОР @pontYGs')
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == 'Список':
        bot.send_message(message.chat.id, 'ВОТ ЦИТАТЫ\n\n-' 'ошибка 228' )
    if message.text == 'Рандом':
        bot.send_message(message.chat.id, 'Я ЗАРАНДОМИЛ ДЛЯ ТЕБЯ ЦИТАТУ: \n\n -' + RandomElement())
    if message.text == 'Добавить':
        bot.send_message(message.chat.id, 'НАПИШИ ЦИТАТУ\n\n- ')
        bot.register_next_step_handler(message,AddElement)
    if message.text == 'Удалить':
        bot.send_message(message.chat.id, 'НАПИШИ ЦИТАТУ, КОТОРУЮ НАДО УДАЛИТЬ\n\n- ')
        bot.register_next_step_handler(message, RemoveElement)
        # Метод для рандомной цитаты
def RandomElement():
    if len(csreturn)!=0:
        index = random.randint(0, len(csreturn) - 1)
        str = csreturn[index]
        csreturn.remove(csreturn[index])
        return str
    else:
        for item in cs:
            csreturn.append(item)
        index = random.randint(0, len(csreturn) - 1)
        str = csreturn[index]
        csreturn.remove(csreturn[index])
        return str
    # Метод для добавление цвета с проверкой на существующие цвета
def AddElement(message):
    global item
    item=message.text
    if not cs.__contains__(item):
        cs.append(item)
        csreturn.append(item)
        bot.send_message(message.from_user.id, f'ДОБАВИЛ ЦИТАТУ\n\n- {message.text}');
    else:
        bot.send_message(message.chat.id, f'ЦИТАТА\n\n- {message.text}\n\n- СУЩЕСТВУЕТ, НАПИШИ ДРУГУЮ\n\n- ')
        bot.register_next_step_handler(message,AddElement)
# Метод для удаления цитат с проверкой на существующей цитаты
def RemoveElement(message):
    global item
    item = message.text
    if cs.__contains__(item):
        cs.remove(item)
        csreturn.remove(item)
        bot.send_message(message.from_user.id, f'УДАЛИЛ ЦИТАТУ\n\n- {message.text}');
    else:
        bot.send_message(message.from_user.id, f'ТАКОЙ ЦЫТАТЫ НЕТУ, МОГУ ДОБАВИТЬ(напиши её)\n\n-');
        bot.register_next_step_handler(message, AddElement)
# Запускаем бота
bot.polling(none_stop=True, interval=0)
