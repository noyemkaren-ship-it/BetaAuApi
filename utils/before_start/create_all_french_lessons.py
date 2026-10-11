
LESSON_1_HTML = """
<div class="lesson-block">

  <div class="lesson-intro">
    <span class="lesson-chip">🇫🇷 Français · Débutant · Урок 1</span>
    <h2>Приветствие и знакомство</h2>
    <p class="lesson-lead">
      <strong>Bonjour !</strong> С этого урока начинается твой путь во французский.
      Здесь ты научишься здороваться, представляться и прощаться — те самые фразы,
      без которых не обходится ни один разговор. К концу урока ты сможешь
      провести мини-диалог с носителем.
    </p>
  </div>

  <div class="lesson-goals">
    <h3>🎯 Что ты узнаешь</h3>
    <ul>
      <li>4 способа поздороваться — и когда какой уместен</li>
      <li>Как представиться и спросить имя собеседника</li>
      <li>3 способа попрощаться</li>
      <li>Правила произношения (с русской транскрипцией)</li>
      <li>Типичные ошибки новичков — чтобы не наступить на грабли</li>
    </ul>
  </div>

  <div class="lesson-section">
    <h3>👋 Шаг 1. Приветствия</h3>
    <p>
      Во французском приветствие зависит от <strong>времени суток</strong>
      и <strong>степени близости</strong>. Это как в русском: «здравствуйте»
      и «привет» — не одно и то же. Просто во французском правил чуть больше.
    </p>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Французский</th>
          <th>Звучит как</th>
          <th>Перевод</th>
          <th>Когда использовать</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Bonjour</strong></td>
          <td><em>бон-ЖУР</em></td>
          <td>Здравствуйте / Добрый день</td>
          <td>Универсально. С 6 утра до 18:00. К любому человеку.</td>
        </tr>
        <tr>
          <td><strong>Bonsoir</strong></td>
          <td><em>бон-СУАР</em></td>
          <td>Добрый вечер</td>
          <td>После 18:00. К любому человеку.</td>
        </tr>
        <tr>
          <td><strong>Salut</strong></td>
          <td><em>са-ЛЮ</em></td>
          <td>Привет</td>
          <td>С друзьями, коллегами, ровесниками. Неформально.</td>
        </tr>
        <tr>
          <td><strong>Coucou</strong></td>
          <td><em>ку-КУ</em></td>
          <td>Приветик</td>
          <td>С близкими: парень, девушка, лучший друг, семья.</td>
        </tr>
      </tbody>
    </table>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">💡</div>
      <div>
        <strong>Почему «bonjour» работает всегда?</strong>
        Дословно оно значит «добрый день». Это нейтральное, вежливое
        приветствие. Если не знаешь, что сказать — говори <em>bonjour</em>.
        Ошибиться невозможно. Единственное исключение — вечером лучше
        <em>bonsoir</em>, но и <em>bonjour</em> вечером поймут (просто
        прозвучит чуть формально).
      </div>
    </div>

    <div class="lesson-callout lesson-callout-warn">
      <div class="callout-icon">⚠️</div>
      <div>
        <strong>Не путай:</strong> <em>bonjour</em> — при встрече.
        <em>Bonne journée</em> (бон жур-НЭ) — при прощании, «хорошего дня».
        Это не приветствие! Если скажешь <em>bonne journée</em> при встрече,
        француз удивится.
      </div>
    </div>

    <div class="lesson-mini-practice">
      <strong>🖊 Мини-практика:</strong>
      Ты заходишь в кафе в 14:00. Что скажешь баристе?
      <br><em>Ответ: Bonjour !</em> (днём, к незнакомому человеку)
    </div>
  </div>

  <div class="lesson-section">
    <h3>🙋 Шаг 2. Как представиться</h3>
    <p>
      Формула простая: <code>Je m'appelle + имя</code>.
      Дословно — «я себя называю». Так же, как русское «меня зовут»,
      только с возвратным глаголом.
    </p>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Французский</th>
          <th>Звучит как</th>
          <th>Перевод</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Je m'appelle Marie.</strong></td>
          <td><em>жё ма-ПЭЛЬ Мари</em></td>
          <td>Меня зовут Мари.</td>
        </tr>
        <tr>
          <td><strong>Je m'appelle Ivan.</strong></td>
          <td><em>жё ма-ПЭЛЬ Иван</em></td>
          <td>Меня зовут Иван.</td>
        </tr>
        <tr>
          <td><strong>Et toi ?</strong></td>
          <td><em>э ТУА</em></td>
          <td>А ты? (неформально)</td>
        </tr>
        <tr>
          <td><strong>Et vous ?</strong></td>
          <td><em>э ВУ</em></td>
          <td>А вы? (вежливо / мн.ч.)</td>
        </tr>
      </tbody>
    </table>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">🔤</div>
      <div>
        <strong>Обрати внимание на апостроф:</strong> <em>je m'appelle</em>,
        а не <s>je me appelle</s>. Перед гласной <em>me → m'</em>.
        Это правило французского языка — «элизия» — работает со всеми
        короткими словами перед гласной.
      </div>
    </div>

    <div class="lesson-mini-practice">
      <strong>🖊 Мини-практика:</strong>
      Скажи вслух: «Меня зовут <твоё имя>. А ты?»
      <br><em>Ответ: Je m'appelle [имя]. Et toi ?</em>
    </div>
  </div>

  <div class="lesson-section">
    <h3>💬 Шаг 3. Живой диалог</h3>
    <p>
      Вот как выглядит знакомство двух людей. Прочитай вслух —
      постарайся повторить интонацию. Во французском интонация часто
      важнее слов: вопрос делается подъёмом голоса в конце.
    </p>

    <div class="lesson-dialog">
      <div class="dialog-line">
        <span class="dialog-avatar">A</span>
        <div class="dialog-bubble">
          <strong>Bonjour !</strong>
          <span>Здравствуйте!</span>
        </div>
      </div>
      <div class="dialog-line dialog-line-right">
        <span class="dialog-avatar">B</span>
        <div class="dialog-bubble">
          <strong>Bonjour ! Je m'appelle Paul. Et toi ?</strong>
          <span>Здравствуйте! Меня зовут Поль. А тебя?</span>
        </div>
      </div>
      <div class="dialog-line">
        <span class="dialog-avatar">A</span>
        <div class="dialog-bubble">
          <strong>Je m'appelle Anna. Enchantée !</strong>
          <span>Меня зовут Анна. Приятно познакомиться!</span>
        </div>
      </div>
      <div class="dialog-line dialog-line-right">
        <span class="dialog-avatar">B</span>
        <div class="dialog-bubble">
          <strong>Enchanté ! À bientôt !</strong>
          <span>Приятно познакомиться! До скорого!</span>
        </div>
      </div>
    </div>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">✨</div>
      <div>
        <strong>Enchanté / Enchantée.</strong> Мужчина говорит <em>enchanté</em>,
        женщина добавляет <em>-e</em>: <em>enchantée</em>. Это «приятно
        познакомиться». Слово буквально значит «очарован(а)». Очень
        вежливо — можно говорить и с друзьями, и на встрече с директором.
      </div>
    </div>
  </div>

  <div class="lesson-section">
    <h3>👋 Шаг 4. Прощание</h3>
    <p>
      Тут правил ещё меньше — главное запомнить 3 варианта и понимать разницу.
    </p>

    <div class="lesson-cards">
      <div class="lesson-mini-card">
        <div class="mini-fr">Au revoir</div>
        <div class="mini-pron">о рё-ВУАР</div>
        <div class="mini-ru">До свидания (универсально)</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">À bientôt</div>
        <div class="mini-pron">а бьен-ТО</div>
        <div class="mini-ru">До скорого (увидимся)</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">Salut</div>
        <div class="mini-pron">са-ЛЮ</div>
        <div class="mini-ru">Пока (неформально)</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">Bonne journée</div>
        <div class="mini-pron">бон жур-НЭ</div>
        <div class="mini-ru">Хорошего дня</div>
      </div>
    </div>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">🎭</div>
      <div>
        <strong>Salut — двойное слово.</strong> Оно работает и как «привет»,
        и как «пока» — в зависимости от контекста. Всё как с итальянским
        «чао». С друзьями это норм, с начальником — не очень.
      </div>
    </div>
  </div>

  <div class="lesson-section">
    <h3>📌 Что запомнить из урока 1</h3>
    <div class="lesson-cards">
      <div class="lesson-mini-card">
        <div class="mini-fr">Bonjour</div>
        <div class="mini-pron">универсальное приветствие</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">Je m'appelle…</div>
        <div class="mini-pron">меня зовут…</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">Et toi ?</div>
        <div class="mini-pron">а ты?</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">Au revoir</div>
        <div class="mini-pron">до свидания</div>
      </div>
    </div>
  </div>

  <div class="lesson-task">
    <div class="task-head">
      <span class="task-badge">Практика</span>
      <h3>Закрепи материал</h3>
    </div>
    <p>Сделай эти 4 задания. Можно вслух, можно в тетради:</p>
    <ol>
      <li>Поздоровайся с коллегой в 20:00. Что скажешь?</li>
      <li>Скажи, что тебя зовут (своё имя) и спроси имя собеседника.</li>
      <li>Попрощайся с другом и пожелай хорошего дня.</li>
      <li>Напиши по памяти диалог из 4 реплик: привет → знакомство → ответ → прощание.</li>
    </ol>
    <p class="task-hint">
      Подсказка: <em>Bonsoir</em>, <em>Je m'appelle … Et toi ?</em>,
      <em>Au revoir, bonne journée !</em>
    </p>
  </div>

  <div class="lesson-finish">
    <span class="finish-emoji">🎉</span>
    <strong>Félicitations !</strong>
    <p>Первый урок позади. Ты уже можешь поздороваться, представиться и попрощаться. Дальше — местоимения и глаголы.</p>
  </div>

</div>
"""


LESSON_2_HTML = """
<div class="lesson-block">

  <div class="lesson-intro">
    <span class="lesson-chip">🇫🇷 Français · Débutant · Урок 2</span>
    <h2>Местоимения и первые глаголы</h2>
    <p class="lesson-lead">
      Теперь, когда ты умеешь здороваться, пора научиться говорить
      о себе и других. В этом уроке — <strong>личные местоимения</strong>,
      <strong>спряжение правильных глаголов</strong> и два самых важных
      неправильных: <em>aller</em> (идти) и <em>être</em> (быть).
      После этого урока ты сможешь строить простые предложения.
    </p>
  </div>

  <div class="lesson-goals">
    <h3>🎯 Что ты узнаешь</h3>
    <ul>
      <li>Все 9 личных местоимений и когда какое использовать</li>
      <li>Как спрягаются правильные глаголы на <em>-er</em> (их 90% всех глаголов)</li>
      <li>Два неправильных, но самых нужных: <em>aller</em> и <em>être</em></li>
      <li>Как строить простое предложение: подлежащее + глагол + дополнение</li>
      <li>Типичные ошибки: где русский и французский расходятся</li>
    </ul>
  </div>

  <div class="lesson-section">
    <h3>👤 Шаг 1. Личные местоимения</h3>
    <p>
      Во французском 9 личных местоимений. Они <strong>всегда</strong>
      стоят перед глаголом — как в русском, но обязательны даже там,
      где мы бы их опустили. Во французском <strong>нельзя</strong> сказать
      просто «говорю» — нужно <em>je parle</em>, «я говорю».
    </p>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Местоимение</th>
          <th>Звучит как</th>
          <th>Перевод</th>
          <th>Комментарий</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>je</strong></td>
          <td><em>жё</em></td>
          <td>я</td>
          <td>Перед гласной → <em>j'</em>: j'aime, j'habite</td>
        </tr>
        <tr>
          <td><strong>tu</strong></td>
          <td><em>тю</em></td>
          <td>ты</td>
          <td>К другу, ровеснику, члену семьи</td>
        </tr>
        <tr>
          <td><strong>il</strong></td>
          <td><em>иль</em></td>
          <td>он</td>
          <td>Только для людей м.р. и животных</td>
        </tr>
        <tr>
          <td><strong>elle</strong></td>
          <td><em>эль</em></td>
          <td>она</td>
          <td>Для людей ж.р. и предметов ж.р.</td>
        </tr>
        <tr>
          <td><strong>nous</strong></td>
          <td><em>ну</em></td>
          <td>мы</td>
          <td>Всегда «мы», не путать с <em>on</em></td>
        </tr>
        <tr>
          <td><strong>vous</strong></td>
          <td><em>ву</em></td>
          <td>вы / Вы</td>
          <td>Мн.ч. ИЛИ вежливо к одному</td>
        </tr>
        <tr>
          <td><strong>ils</strong></td>
          <td><em>иль</em></td>
          <td>они (м.р. или смеш.)</td>
          <td>Даже 1 парень + 99 девушек = ils</td>
        </tr>
        <tr>
          <td><strong>elles</strong></td>
          <td><em>эль</em></td>
          <td>они (ж.р.)</td>
          <td>Только если все — женщины</td>
        </tr>
        <tr>
          <td><strong>on</strong></td>
          <td><em>он</em></td>
          <td>мы / люди / кто-то</td>
          <td>Разговорное «мы», глагол как у il/elle</td>
        </tr>
      </tbody>
    </table>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">💡</div>
      <div>
        <strong>Про «vous»:</strong> это аналог русского «вы» — и для
        множественного числа, и для вежливого обращения к одному человеку.
        Разница: во Франции «vous» используют <strong>чаще</strong>, чем
        в России. К незнакомым, к старшим, к коллегам по умолчанию — <em>vous</em>.
        На «tu» переходят только когда собеседник сам предложит.
      </div>
    </div>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">🎭</div>
      <div>
        <strong>Про «on»:</strong> формально означает «люди» или «некто».
        <em>On dit que…</em> — «Говорят, что…». Но в разговорной речи
        французы постоянно используют <em>on</em> вместо <em>nous</em>:
        <em>On va au cinéma</em> = «Мы идём в кино». Глагол при этом
        ставится в форму <strong>il/elle</strong>.
      </div>
    </div>

    <div class="lesson-mini-practice">
      <strong>🖊 Мини-практика:</strong>
      Какое местоимение использовать?
      <br>1) Ты говоришь с директором → <em>vous</em>
      <br>2) Ты говоришь с другом → <em>tu</em>
      <br>3) Маша и Катя (обе девушки) → <em>elles</em>
      <br>4) Маша и Петя → <em>ils</em>
    </div>
  </div>

  <div class="lesson-section">
    <h3>🔤 Шаг 2. Правильные глаголы на -er</h3>
    <p>
      Это <strong>самая большая группа</strong> французских глаголов —
      около 90%. Они называются «правильными», потому что спрягаются
      по одной и той же схеме. Запомнив схему один раз, ты сможешь
      спрягать <strong>тысячи</strong> глаголов.
    </p>

    <p>
      <strong>Как работает схема:</strong> берём инфинитив (parler = говорить),
      отрезаем окончание <code>-er</code>, получаем основу (<em>parl-</em>),
      и добавляем к ней нужное окончание.
    </p>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Местоимение</th>
          <th>Окончание</th>
          <th>Форма parler</th>
          <th>Перевод</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>je</td><td><strong>-e</strong></td><td>je parl<strong>e</strong></td><td>я говорю</td></tr>
        <tr><td>tu</td><td><strong>-es</strong></td><td>tu parl<strong>es</strong></td><td>ты говоришь</td></tr>
        <tr><td>il / elle / on</td><td><strong>-e</strong></td><td>il parl<strong>e</strong></td><td>он говорит</td></tr>
        <tr><td>nous</td><td><strong>-ons</strong></td><td>nous parl<strong>ons</strong></td><td>мы говорим</td></tr>
        <tr><td>vous</td><td><strong>-ez</strong></td><td>vous parl<strong>ez</strong></td><td>вы говорите</td></tr>
        <tr><td>ils / elles</td><td><strong>-ent</strong></td><td>ils parl<strong>ent</strong></td><td>они говорят</td></tr>
      </tbody>
    </table>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">🔇</div>
      <div>
        <strong>Хитрость произношения:</strong> окончания <strong>-e</strong>,
        <strong>-es</strong> и <strong>-ent</strong> — немые. То есть
        <em>je parle</em>, <em>tu parles</em> и <em>ils parlent</em>
        звучат <strong>одинаково</strong>: «парль». Различить их можно
        только по местоимению. А вот <em>nous parlons</em> («пар-ЛОН») и
        <em>vous parlez</em> («пар-ЛЭ») слышны отчётливо.
      </div>
    </div>

    <p><strong>Другие частые глаголы на -er:</strong></p>

    <div class="lesson-cards">
      <div class="lesson-mini-card">
        <div class="mini-fr">aimer</div>
        <div class="mini-pron">э-МЭ</div>
        <div class="mini-ru">любить</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">habiter</div>
        <div class="mini-pron">а-би-ТЭ</div>
        <div class="mini-ru">жить (где-то)</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">travailler</div>
        <div class="mini-pron">тра-ва-ЙЕ</div>
        <div class="mini-ru">работать</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">étudier</div>
        <div class="mini-pron">э-тю-ДЬЕ</div>
        <div class="mini-ru">учиться</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">regarder</div>
        <div class="mini-pron">рё-гар-ДЭ</div>
        <div class="mini-ru">смотреть</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">écouter</div>
        <div class="mini-pron">э-ку-ТЭ</div>
        <div class="mini-ru">слушать</div>
      </div>
    </div>

    <div class="lesson-mini-practice">
      <strong>🖊 Мини-практика:</strong>
      Проспрягай <em>aimer</em> (любить) по всем лицам:
      <br>je <em>aime</em> · tu <em>aimes</em> · il <em>aime</em> ·
      nous <em>aimons</em> · vous <em>aimez</em> · ils <em>aiment</em>
    </div>
  </div>

  <div class="lesson-section">
    <h3>🚶 Шаг 3. Неправильный глагол: aller (идти)</h3>
    <p>
      <strong>Aller</strong> — один из самых частых глаголов французского,
      и полностью неправильный. Окончания как у <em>-er</em> группы не работают —
      формы надо выучить наизусть. Хорошая новость: их всего 6.
    </p>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Местоимение</th>
          <th>Форма</th>
          <th>Звучит как</th>
          <th>Перевод</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>je</td><td><strong>vais</strong></td><td><em>вэ</em></td><td>я иду / еду</td></tr>
        <tr><td>tu</td><td><strong>vas</strong></td><td><em>ва</em></td><td>ты идёшь</td></tr>
        <tr><td>il / elle</td><td><strong>va</strong></td><td><em>ва</em></td><td>он/она идёт</td></tr>
        <tr><td>nous</td><td><strong>allons</strong></td><td><em>а-ЛОН</em></td><td>мы идём</td></tr>
        <tr><td>vous</td><td><strong>allez</strong></td><td><em>а-ЛЭ</em></td><td>вы идёте</td></tr>
        <tr><td>ils / elles</td><td><strong>vont</strong></td><td><em>вон</em></td><td>они идут</td></tr>
      </tbody>
    </table>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">💡</div>
      <div>
        <strong>Aller = идти И ехать.</strong> В русском мы различаем
        «идти пешком» и «ехать на транспорте». Во французском — одно
        слово <em>aller</em> для всего. <em>Je vais à Paris</em> = «Я еду
        в Париж». <em>Je vais à l'école</em> = «Я иду в школу».
      </div>
    </div>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">📌</div>
      <div>
        <strong>Запомни конструкцию:</strong> <em>aller à + место</em>.
        <em>Je vais à Paris</em> — в Париж. <em>à</em> может сокращаться:
        <em>à + le = au</em>, <em>à + les = aux</em>. Это как «в + дом = домой»
        в русском.
      </div>
    </div>

    <div class="lesson-mini-practice">
      <strong>🖊 Мини-практика:</strong>
      Переведи на французский:
      <br>1) Я иду в школу → <em>Je vais à l'école</em>
      <br>2) Мы едем в Париж → <em>Nous allons à Paris</em>
      <br>3) Они идут домой → <em>Ils vont à la maison</em>
    </div>
  </div>

  <div class="lesson-section">
    <h3>✨ Шаг 4. Неправильный глагол: être (быть)</h3>
    <p>
      <strong>Être</strong> — самый важный глагол французского.
      Без него не построить даже простейшее предложение.
      Тоже полностью неправильный. Формы надо знать наизусть.
    </p>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Местоимение</th>
          <th>Форма</th>
          <th>Звучит как</th>
          <th>Перевод</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>je</td><td><strong>suis</strong></td><td><em>сюи</em></td><td>я есть</td></tr>
        <tr><td>tu</td><td><strong>es</strong></td><td><em>э</em></td><td>ты есть</td></tr>
        <tr><td>il / elle</td><td><strong>est</strong></td><td><em>э</em></td><td>он/она есть</td></tr>
        <tr><td>nous</td><td><strong>sommes</strong></td><td><em>сом</em></td><td>мы есть</td></tr>
        <tr><td>vous</td><td><strong>êtes</strong></td><td><em>эт</em></td><td>вы есть</td></tr>
        <tr><td>ils / elles</td><td><strong>sont</strong></td><td><em>сон</em></td><td>они есть</td></tr>
      </tbody>
    </table>

    <div class="lesson-callout lesson-callout-warn">
      <div class="callout-icon">🇷🇺</div>
      <div>
        <strong>Главная ловушка для русских:</strong> в русском мы говорим
        «Я студент» — <strong>без</strong> глагола «быть» в настоящем.
        Во французском глагол обязателен: <em>Je suis étudiant</em>.
        Дословно «Я есть студент». То же самое:
        <em>Il est russe</em> = «Он русский»,
        <em>Nous sommes ici</em> = «Мы здесь».
      </div>
    </div>

    <div class="lesson-mini-practice">
      <strong>🖊 Мини-практика:</strong>
      Переведи:
      <br>1) Я студент → <em>Je suis étudiant</em>
      <br>2) Ты француз? → <em>Tu es français ?</em>
      <br>3) Мы здесь → <em>Nous sommes ici</em>
      <br>4) Она врач → <em>Elle est médecin</em>
    </div>
  </div>

  <div class="lesson-section">
    <h3>💬 Шаг 5. Собираем предложения</h3>
    <p>
      Теперь у тебя есть всё, чтобы строить простые фразы. Схема простая:
    </p>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">🧩</div>
      <div style="text-align:center; font-size: 1.05rem;">
        <strong>Подлежащее + глагол + дополнение</strong><br>
        <em>Je</em> + <em>parle</em> + <em>français</em><br>
        <em>Nous</em> + <em>allons</em> + <em>à Paris</em>
      </div>
    </div>

    <p>Вот примеры со всеми глаголами, которые ты выучил:</p>

    <div class="lesson-examples">
      <div class="example-row">
        <div class="example-fr">Je suis étudiant.</div>
        <div class="example-ru">Я студент.</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Tu es français ?</div>
        <div class="example-ru">Ты француз?</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Elle va à Paris.</div>
        <div class="example-ru">Она едет в Париж.</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Nous parlons français.</div>
        <div class="example-ru">Мы говорим по-французски.</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Ils vont à l'école.</div>
        <div class="example-ru">Они идут в школу.</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Vous êtes russes ?</div>
        <div class="example-ru">Вы русские?</div>
      </div>
      <div class="example-row">
        <div class="example-fr">J'habite à Moscou.</div>
        <div class="example-ru">Я живу в Москве.</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Elle aime le café.</div>
        <div class="example-ru">Она любит кофе.</div>
      </div>
    </div>
  </div>

  <div class="lesson-callout lesson-callout-warn">
    <div class="callout-icon">⚠️</div>
    <div>
      <strong>Элизия (сокращение):</strong> перед гласной или немой <em>h</em>
      короткие слова теряют последнюю гласную и берут апостроф.
      <em>je + aime → j'aime</em>. <em>je + habite → j'habite</em>.
      Это <strong>обязательно</strong>, не стилистика. <s>Je aime</s> —
      грубая ошибка.
    </div>
  </div>

  <div class="lesson-section">
    <h3>📌 Что запомнить из урока 2</h3>
    <div class="lesson-cards">
      <div class="lesson-mini-card">
        <div class="mini-fr">je, tu, il…</div>
        <div class="mini-pron">9 местоимений</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">-e, -es, -ons…</div>
        <div class="mini-pron">окончания -er</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">vais, vas, va…</div>
        <div class="mini-pron">aller (идти)</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">suis, es, est…</div>
        <div class="mini-pron">être (быть)</div>
      </div>
    </div>
  </div>

  <div class="lesson-task">
    <div class="task-head">
      <span class="task-badge">Практика</span>
      <h3>Закрепи материал</h3>
    </div>
    <p>Переведи на французский (вслух или в тетради):</p>
    <ol>
      <li>Я живу в Москве. <em>(habiter)</em></li>
      <li>Он говорит по-французски. <em>(parler)</em></li>
      <li>Мы идём в школу. <em>(aller)</em></li>
      <li>Ты студент? <em>(être)</em></li>
      <li>Они любят кофе. <em>(aimer)</em></li>
      <li>Вы французы? <em>(être)</em></li>
    </ol>
    <p class="task-hint">
      Подсказка: <em>J'habite à Moscou · Il parle français · Nous allons à l'école · Tu es étudiant ? · Ils aiment le café · Vous êtes français ?</em>
    </p>
  </div>

  <div class="lesson-finish">
    <span class="finish-emoji">🎉</span>
    <strong>Bravo !</strong>
    <p>Ты освоил местоимения и первые глаголы. Теперь можешь строить простые предложения. Дальше — существительные и контрольная.</p>
  </div>

</div>
"""



# =====================================================================
# УРОК 3 — СУЩЕСТВИТЕЛЬНЫЕ И КОНТРОЛЬНАЯ
# =====================================================================

LESSON_3_HTML = """
<div class="lesson-block">

  <div class="lesson-intro">
    <span class="lesson-chip">🇫🇷 Français · Débutant · Урок 3</span>
    <h2>Существительные и контрольная</h2>
    <p class="lesson-lead">
      Сегодня — <strong>самые нужные существительные</strong>, ещё несколько
      глаголов, и в конце — <strong>интерактивная контрольная</strong> в стиле
      Duolingo: собирай предложения из «кирпичиков». К концу урока ты будешь
      говорить полными фразами.
    </p>
  </div>

  <div class="lesson-goals">
    <h3>🎯 Что ты узнаешь</h3>
    <ul>
      <li>Род существительных: как определить le / la / l'</li>
      <li>10 самых нужных существительных на каждый день</li>
      <li>6 новых глаголов + неправильный <em>avoir</em> (иметь)</li>
      <li>Как сказать «у меня есть…» — очень важная конструкция</li>
      <li>Соберёшь предложения в интерактивной контрольной</li>
    </ul>
  </div>

  <div class="lesson-section">
    <h3>📦 Шаг 1. Род существительных: le / la / les</h3>
    <p>
      Во французском у каждого существительного есть <strong>род</strong> —
      мужской или женский. Род показывается <strong>артиклем</strong> перед
      словом. В русском тоже есть род, но во французском он <strong>не всегда
      совпадает</strong> с русским — и это главная сложность для новичка.
    </p>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Артикль</th>
          <th>Когда использовать</th>
          <th>Пример</th>
          <th>Перевод</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>le</strong></td>
          <td>мужской род, ед.ч.</td>
          <td>le livre</td>
          <td>книга</td>
        </tr>
        <tr>
          <td><strong>la</strong></td>
          <td>женский род, ед.ч.</td>
          <td>la table</td>
          <td>стол</td>
        </tr>
        <tr>
          <td><strong>les</strong></td>
          <td>мн. число (любой род)</td>
          <td>les livres</td>
          <td>книги</td>
        </tr>
        <tr>
          <td><strong>l'</strong></td>
          <td>перед гласной или немой h</td>
          <td>l'ami, l'école</td>
          <td>друг, школа</td>
        </tr>
      </tbody>
    </table>

    <div class="lesson-callout lesson-callout-warn">
      <div class="callout-icon">⚠️</div>
      <div>
        <strong>Род не совпадает с русским!</strong><br>
        <em>La table</em> (стол) — женского рода, хотя в русском «стол» — мужского.<br>
        <em>Le livre</em> (книга) — мужского, хотя «книга» — женского.<br>
        <em>La ville</em> (город) — женского.<br>
        Род надо запоминать <strong>вместе со словом</strong> — как в русском
        мы запоминаем, что «пальто» среднего рода.
      </div>
    </div>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">🧠</div>
      <div>
        <strong>Подсказки для запоминания:</strong> слова на <em>-tion</em>,
        <em>-té</em>, <em>-ette</em> — почти всегда женские:
        <em>la nation, la beauté, la maisonnette</em>. Слова на
        <em>-ment</em>, <em>-age</em>, <em>-eau</em> — мужские:
        <em>le mouvement, le voyage, le bateau</em>. Это работает для
        большинства слов, но не для всех.
      </div>
    </div>

    <div class="lesson-mini-practice">
      <strong>🖊 Мини-практика:</strong>
      Угадай род (le или la):
      <br>_ maison (дом) → <em>la</em>
      <br>_ chat (кот) → <em>le</em>
      <br>_ ville (город) → <em>la</em>
      <br>_ livre (книга) → <em>le</em>
    </div>
  </div>

  <div class="lesson-section">
    <h3>📚 Шаг 2. Полезные существительные</h3>
    <p>
      10 слов, которые встречаются каждый день. Запомни их <strong>вместе
      с артиклем</strong> — так правильно.
    </p>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Французский</th>
          <th>Звучит как</th>
          <th>Перевод</th>
          <th>Род</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>le livre</strong></td><td><em>лё ливр</em></td><td>книга</td><td>м.р.</td></tr>
        <tr><td><strong>la table</strong></td><td><em>ля табль</em></td><td>стол</td><td>ж.р.</td></tr>
        <tr><td><strong>la maison</strong></td><td><em>ля мэ-ЗОН</em></td><td>дом</td><td>ж.р.</td></tr>
        <tr><td><strong>l'école</strong></td><td><em>лэ-КОЛЬ</em></td><td>школа</td><td>ж.р.</td></tr>
        <tr><td><strong>le chat</strong></td><td><em>лё ша</em></td><td>кот</td><td>м.р.</td></tr>
        <tr><td><strong>le chien</strong></td><td><em>лё шьен</em></td><td>собака</td><td>м.р.</td></tr>
        <tr><td><strong>l'ami / l'amie</strong></td><td><em>ля-МИ</em></td><td>друг / подруга</td><td>м./ж.</td></tr>
        <tr><td><strong>le travail</strong></td><td><em>лё тра-ВАЙ</em></td><td>работа</td><td>м.р.</td></tr>
        <tr><td><strong>la ville</strong></td><td><em>ля виль</em></td><td>город</td><td>ж.р.</td></tr>
        <tr><td><strong>le pays</strong></td><td><em>лё пэ-И</em></td><td>страна</td><td>м.р.</td></tr>
      </tbody>
    </table>
  </div>

  <div class="lesson-section">
    <h3>🔤 Шаг 3. Ещё глаголы</h3>
    <p>6 новых глаголов для повседневных ситуаций:</p>

    <div class="lesson-cards">
      <div class="lesson-mini-card">
        <div class="mini-fr">avoir</div>
        <div class="mini-pron">а-ВУАР</div>
        <div class="mini-ru">иметь</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">faire</div>
        <div class="mini-pron">фэр</div>
        <div class="mini-ru">делать</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">manger</div>
        <div class="mini-pron">ман-ЖЕ</div>
        <div class="mini-ru">есть, кушать</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">voir</div>
        <div class="mini-pron">вуар</div>
        <div class="mini-ru">видеть</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">venir</div>
        <div class="mini-pron">вё-НИР</div>
        <div class="mini-ru">приходить</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">lire</div>
        <div class="mini-pron">лир</div>
        <div class="mini-ru">читать</div>
      </div>
    </div>

    <p style="margin-top:22px;">
      <strong>Avoir</strong> (иметь) — неправильный, но безумно нужный.
      Спрягается так:
    </p>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Местоимение</th>
          <th>Форма</th>
          <th>Звучит как</th>
          <th>Перевод</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>j'</td><td><strong>ai</strong></td><td><em>жэ</em></td><td>я имею</td></tr>
        <tr><td>tu</td><td><strong>as</strong></td><td><em>тю а</em></td><td>ты имеешь</td></tr>
        <tr><td>il / elle</td><td><strong>a</strong></td><td><em>иль а</em></td><td>он/она имеет</td></tr>
        <tr><td>nous</td><td><strong>avons</strong></td><td><em>ну а-ВОН</em></td><td>мы имеем</td></tr>
        <tr><td>vous</td><td><strong>avez</strong></td><td><em>ву а-ВЭ</em></td><td>вы имеете</td></tr>
        <tr><td>ils / elles</td><td><strong>ont</strong></td><td><em>иль зон</em></td><td>они имеют</td></tr>
      </tbody>
    </table>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">🇷🇺</div>
      <div>
        <strong>Как сказать «у меня есть»?</strong> Во французском нет
        отдельного слова «у». Говорят буквально «я имею»:
        <em>J'ai un chat</em> = «У меня есть кот» (дословно «Я имею кота»).
        Это как в английском <em>I have</em>.
      </div>
    </div>
  </div>

  <div class="lesson-section">
    <h3>💬 Шаг 4. Примеры с существительными</h3>

    <div class="lesson-examples">
      <div class="example-row">
        <div class="example-fr">J'ai un chat.</div>
        <div class="example-ru">У меня есть кот.</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Elle a une maison.</div>
        <div class="example-ru">У неё есть дом.</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Nous mangeons à la maison.</div>
        <div class="example-ru">Мы едим дома.</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Ils lisent un livre.</div>
        <div class="example-ru">Они читают книгу.</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Tu vois la ville ?</div>
        <div class="example-ru">Ты видишь город?</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Je viens de Moscou.</div>
        <div class="example-ru">Я из Москвы.</div>
      </div>
    </div>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">💡</div>
      <div>
        <strong>Заметь:</strong> после <em>avoir</em> артикль не исчезает,
        как в русском («у меня <strong>есть</strong> кот» — без артикля).
        Во французском: <em>J'ai <strong>un</strong> chat</em> —
        с неопределённым артиклем. Он обязателен.
      </div>
    </div>
  </div>

  <!-- === КОНТРОЛЬНАЯ === -->
  <div class="lesson-quiz">
    <div class="quiz-head">
      <span class="quiz-badge">Контрольная</span>
      <h3>Собери предложения</h3>
      <p class="text-muted">Нажимай на кирпичики, чтобы построить перевод. Клик по выбранному слову — вернуть обратно.</p>
    </div>

    <div id="quiz-container"></div>

    <div class="quiz-finish hidden" id="quiz-finish">
      <span class="finish-emoji">🏆</span>
      <strong>Контрольная пройдена!</strong>
      <p id="quiz-score"></p>
    </div>
  </div>

  <div class="lesson-section" style="margin-top:32px;">
    <h3>📌 Что запомнить из урока 3</h3>
    <div class="lesson-cards">
      <div class="lesson-mini-card">
        <div class="mini-fr">le / la / les</div>
        <div class="mini-pron">артикли рода</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">J'ai…</div>
        <div class="mini-pron">у меня есть…</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">un / une</div>
        <div class="mini-pron">один / одна (артикль)</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">avoir</div>
        <div class="mini-pron">иметь (неправильный)</div>
      </div>
    </div>
  </div>

  <div class="lesson-finish">
    <span class="finish-emoji">🎉</span>
    <strong>Félicitations !</strong>
    <p>Ты закончил третий урок. Теперь говоришь полными предложениями и знаешь сотни комбинаций. Дальше — числа, дни недели, вопросы.</p>
  </div>

</div>

<script>
(function () {
    var container = document.getElementById('quiz-container');
    if (!container) return;

    var QUESTIONS = [
        {
            prompt: 'Переведи на французский',
            ru: 'Я студент',
            words: ['Je', 'suis', 'étudiant', 'es', 'un'],
            answer: ['Je', 'suis', 'étudiant']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'У меня есть кот',
            words: ['J\\'', 'ai', 'un', 'chat', 'suis', 'le'],
            answer: ['J\\'', 'ai', 'un', 'chat']
        },
        {
            prompt: 'Переведи на русский',
            ru: 'Elle va à Paris',
            words: ['Она', 'едет', 'в', 'Париж', 'идёт', 'живёт'],
            answer: ['Она', 'едет', 'в', 'Париж']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'Мы говорим по-французски',
            words: ['Nous', 'parlons', 'français', 'parlez', 'sommes'],
            answer: ['Nous', 'parlons', 'français']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'Они идут в школу',
            words: ['Ils', 'vont', 'à', 'l\\'école', 'vais', 'le'],
            answer: ['Ils', 'vont', 'à', 'l\\'école']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'Ты видишь город?',
            words: ['Tu', 'vois', 'la', 'ville', 'le', 'voit'],
            answer: ['Tu', 'vois', 'la', 'ville']
        },
        {
            prompt: 'Переведи на русский',
            ru: 'J\\'ai une maison',
            words: ['У', 'меня', 'есть', 'дом', 'кот', 'город'],
            answer: ['У', 'меня', 'есть', 'дом']
        }
    ];

    var current = 0;
    var correctCount = 0;

    function render() {
        if (current >= QUESTIONS.length) {
            showFinish();
            return;
        }

        var q = QUESTIONS[current];
        var html = '';

        html += '<div class="quiz-question">';
        html += '<div class="quiz-progress">Вопрос ' + (current + 1) + ' из ' + QUESTIONS.length + '</div>';
        html += '<div class="quiz-prompt">' + q.prompt + '</div>';
        html += '<div class="quiz-ru">«' + q.ru + '»</div>';
        html += '<div class="quiz-answer" id="quiz-answer" data-placeholder="Нажимай на кирпичики ниже"></div>';

        var shuffled = q.words.slice().sort(function () { return Math.random() - 0.5; });

        html += '<div class="quiz-words" id="quiz-words">';
        shuffled.forEach(function (w) {
            html += '<button type="button" class="quiz-word" data-word="' + w + '">' + w + '</button>';
        });
        html += '</div>';

        html += '<div class="quiz-actions">';
        html += '<button type="button" class="btn btn-ghost" id="quiz-skip">Пропустить</button>';
        html += '<button type="button" class="btn btn-primary" id="quiz-check" disabled>Проверить</button>';
        html += '</div>';

        html += '<div class="quiz-feedback hidden" id="quiz-feedback"></div>';
        html += '</div>';

        container.innerHTML = html;
        bindEvents();
    }

    function bindEvents() {
        var answerZone = document.getElementById('quiz-answer');
        var wordsZone = document.getElementById('quiz-words');
        var checkBtn = document.getElementById('quiz-check');
        var skipBtn = document.getElementById('quiz-skip');
        var feedback = document.getElementById('quiz-feedback');
        var q = QUESTIONS[current];

        function updateCheck() {
            var picked = answerZone.querySelectorAll('.quiz-word').length;
            checkBtn.disabled = picked === 0;
        }

        wordsZone.addEventListener('click', function (e) {
            var btn = e.target.closest('.quiz-word');
            if (!btn || btn.disabled) return;
            var clone = document.createElement('button');
            clone.type = 'button';
            clone.className = 'quiz-word quiz-word-picked';
            clone.setAttribute('data-word', btn.getAttribute('data-word'));
            clone.textContent = btn.textContent;
            answerZone.appendChild(clone);
            btn.style.visibility = 'hidden';
            btn.disabled = true;
            updateCheck();
        });

        answerZone.addEventListener('click', function (e) {
            var btn = e.target.closest('.quiz-word');
            if (!btn) return;
            var word = btn.getAttribute('data-word');
            var source = Array.from(wordsZone.querySelectorAll('.quiz-word'))
                .find(function (b) {
                    return b.getAttribute('data-word') === word && b.disabled;
                });
            if (source) {
                source.style.visibility = 'visible';
                source.disabled = false;
            }
            btn.remove();
            updateCheck();
        });

        checkBtn.addEventListener('click', function () {
            var picked = Array.from(answerZone.querySelectorAll('.quiz-word'))
                .map(function (b) { return b.getAttribute('data-word'); });

            var isCorrect = picked.length === q.answer.length &&
                picked.every(function (w, i) { return w === q.answer[i]; });

            if (isCorrect) {
                correctCount++;
                showFeedback(true, 'Правильно! 🎉');
            } else {
                showFeedback(false, 'Не совсем. Правильно: ' + q.answer.join(' '));
            }

            checkBtn.disabled = true;
            skipBtn.disabled = true;

            setTimeout(function () {
                current++;
                render();
            }, 1500);
        });

        skipBtn.addEventListener('click', function () {
            showFeedback(false, 'Правильный ответ: ' + q.answer.join(' '));
            checkBtn.disabled = true;
            skipBtn.disabled = true;
            setTimeout(function () {
                current++;
                render();
            }, 1500);
        });

        function showFeedback(ok, text) {
            feedback.textContent = text;
            feedback.className = 'quiz-feedback ' + (ok ? 'quiz-feedback-ok' : 'quiz-feedback-no');
        }
    }

    function showFinish() {
        container.classList.add('hidden');
        var finish = document.getElementById('quiz-finish');
        finish.classList.remove('hidden');
        var score = document.getElementById('quiz-score');
        score.textContent = 'Правильных ответов: ' + correctCount + ' из ' + QUESTIONS.length;
    }

    render();
})();
</script>
"""

LESSON_4_HTML = """
<div class="lesson-block">

  <div class="lesson-intro">
    <span class="lesson-chip">🇫🇷 Français · Débutant · Урок 4</span>
    <h2>Числа, дни недели и время</h2>
    <p class="lesson-lead">
      Сегодня ты научишься считать, называть дни недели, месяцы и говорить
      о времени. Это базовый минимум, без которого не обойтись ни в магазине,
      ни в разговоре о планах. А ещё — <strong>интерактивная контрольная</strong>
      в конце, чтобы всё закрепить.
    </p>
  </div>

  <div class="lesson-goals">
    <h3>🎯 Что ты узнаешь</h3>
    <ul>
      <li>Числа от 0 до 100 — и почему 80 считается «сложно»</li>
      <li>Все 7 дней недели и 12 месяцев</li>
      <li>Как спросить и сказать время</li>
      <li>Полезные фразы: «сегодня», «завтра», «вчера»</li>
      <li>Соберёшь предложения в интерактивной контрольной</li>
    </ul>
  </div>

  <div class="lesson-section">
    <h3>🔢 Шаг 1. Числа от 0 до 20</h3>
    <p>
      Числа — это фундамент. Без них не купишь хлеб, не скажешь свой возраст
      и не назначишь встречу. Начнём с базы — от 0 до 20.
      Запомни первые 10, дальше будет легче.
    </p>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Число</th>
          <th>Французский</th>
          <th>Звучит как</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>0</td><td><strong>zéro</strong></td><td><em>зэ-РО</em></td></tr>
        <tr><td>1</td><td><strong>un</strong></td><td><em>эн</em></td></tr>
        <tr><td>2</td><td><strong>deux</strong></td><td><em>дё</em></td></tr>
        <tr><td>3</td><td><strong>trois</strong></td><td><em>труа</em></td></tr>
        <tr><td>4</td><td><strong>quatre</strong></td><td><em>катр</em></td></tr>
        <tr><td>5</td><td><strong>cinq</strong></td><td><em>сэнк</em></td></tr>
        <tr><td>6</td><td><strong>six</strong></td><td><em>сис</em></td></tr>
        <tr><td>7</td><td><strong>sept</strong></td><td><em>сэт</em></td></tr>
        <tr><td>8</td><td><strong>huit</strong></td><td><em>юит</em></td></tr>
        <tr><td>9</td><td><strong>neuf</strong></td><td><em>нёф</em></td></tr>
        <tr><td>10</td><td><strong>dix</strong></td><td><em>дис</em></td></tr>
        <tr><td>11</td><td><strong>onze</strong></td><td><em>онз</em></td></tr>
        <tr><td>12</td><td><strong>douze</strong></td><td><em>дуз</em></td></tr>
        <tr><td>13</td><td><strong>treize</strong></td><td><em>трэз</em></td></tr>
        <tr><td>14</td><td><strong>quatorze</strong></td><td><em>ка-ТОРЗ</em></td></tr>
        <tr><td>15</td><td><strong>quinze</strong></td><td><em>кэнз</em></td></tr>
        <tr><td>16</td><td><strong>seize</strong></td><td><em>сэз</em></td></tr>
        <tr><td>17</td><td><strong>dix-sept</strong></td><td><em>ди-СЭТ</em></td></tr>
        <tr><td>18</td><td><strong>dix-huit</strong></td><td><em>ди-ЗЮИТ</em></td></tr>
        <tr><td>19</td><td><strong>dix-neuf</strong></td><td><em>ди-ЗНЁФ</em></td></tr>
        <tr><td>20</td><td><strong>vingt</strong></td><td><em>вэн</em></td></tr>
      </tbody>
    </table>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">💡</div>
      <div>
        <strong>Логика после 16:</strong> 17, 18, 19 — это «десять + семь»,
        «десять + восемь», «десять + девять». Как в русском «семнадцать» =
        «семь на десять». Запомни схему — и считаешь до 20 без проблем.
      </div>
    </div>

    <div class="lesson-mini-practice">
      <strong>🖊 Мини-практика:</strong>
      Скажи вслух свой возраст, используя <em>J'ai … ans</em>:
      <br><em>J'ai vingt ans</em> — Мне 20 лет.
      <br><em>J'ai trente ans</em> — Мне 30 лет.
    </div>
  </div>

  <div class="lesson-section">
    <h3>🔟 Шаг 2. Десятки и сотни</h3>
    <p>
      После 20 логика простая: десятки + единицы. Например,
      <em>vingt et un</em> = 21, <em>vingt-deux</em> = 22.
      Но есть <strong>одна ловушка</strong> — число 80.
    </p>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Число</th>
          <th>Французский</th>
          <th>Звучит как</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>20</td><td><strong>vingt</strong></td><td><em>вэн</em></td></tr>
        <tr><td>30</td><td><strong>trente</strong></td><td><em>трант</em></td></tr>
        <tr><td>40</td><td><strong>quarante</strong></td><td><em>ка-РАНТ</em></td></tr>
        <tr><td>50</td><td><strong>cinquante</strong></td><td><em>сэн-КАНТ</em></td></tr>
        <tr><td>60</td><td><strong>soixante</strong></td><td><em>суа-САНТ</em></td></tr>
        <tr><td>70</td><td><strong>soixante-dix</strong></td><td><em>суа-сант-ДИС</em></td></tr>
        <tr><td>80</td><td><strong>quatre-vingts</strong></td><td><em>катр-ВЭН</em></td></tr>
        <tr><td>90</td><td><strong>quatre-vingt-dix</strong></td><td><em>катр-вэн-ДИС</em></td></tr>
        <tr><td>100</td><td><strong>cent</strong></td><td><em>сан</em></td></tr>
      </tbody>
    </table>

    <div class="lesson-callout lesson-callout-warn">
      <div class="callout-icon">⚠️</div>
      <div>
        <strong>Почему 80 — «сложное»?</strong> Французы считают не «восемьдесят»,
        а «четыре двадцатки»: <em>quatre-vingts</em> = 4 × 20. А 90 —
        «четыре двадцатки и десять»: <em>quatre-vingt-dix</em>.
        Это наследие кельтского счёта. Просто запомни — логики тут нет.
      </div>
    </div>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">💡</div>
      <div>
        <strong>21, 31, 41…</strong> — используем <em>et un</em>:
        <em>vingt et un</em>, <em>trente et un</em>.
        Но <strong>не</strong> говорим <s>quatre-vingt et un</s> —
        правильно <em>quatre-vingt-un</em> (без «et»).
      </div>
    </div>

    <div class="lesson-mini-practice">
      <strong>🖊 Мини-практика:</strong>
      Напиши цифрами:
      <br><em>quarante-cinq</em> → 45
      <br><em>soixante-douze</em> → 72
      <br><em>quatre-vingt-trois</em> → 83
      <br><em>quatre-vingt-dix-neuf</em> → 99
    </div>
  </div>

  <div class="lesson-section">
    <h3>📅 Шаг 3. Дни недели</h3>
    <p>
      Все дни недели — <strong>мужского рода</strong> и пишутся
      <strong>с маленькой буквы</strong> (в отличие от русского и английского).
    </p>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Французский</th>
          <th>Звучит как</th>
          <th>Перевод</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>lundi</strong></td><td><em>лэн-ДИ</em></td><td>понедельник</td></tr>
        <tr><td><strong>mardi</strong></td><td><em>мар-ДИ</em></td><td>вторник</td></tr>
        <tr><td><strong>mercredi</strong></td><td><em>мер-крё-ДИ</em></td><td>среда</td></tr>
        <tr><td><strong>jeudi</strong></td><td><em>жё-ДИ</em></td><td>четверг</td></tr>
        <tr><td><strong>vendredi</strong></td><td><em>ван-дрё-ДИ</em></td><td>пятница</td></tr>
        <tr><td><strong>samedi</strong></td><td><em>сам-ДИ</em></td><td>суббота</td></tr>
        <tr><td><strong>dimanche</strong></td><td><em>ди-МАНШ</em></td><td>воскресенье</td></tr>
      </tbody>
    </table>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">🗓</div>
      <div>
        <strong>Запомни:</strong> французская неделя начинается с
        <strong>понедельника</strong> (lundi), а не с воскресенья.
        И все дни — с маленькой буквы. <em>lundi</em>, а не <s>Lundi</s>.
      </div>
    </div>

    <div class="lesson-mini-practice">
      <strong>🖊 Мини-практика:</strong>
      Ответь на вопрос:
      <br><em>Quel jour sommes-nous ?</em> — Какой сегодня день?
      <br>→ <em>Nous sommes lundi.</em> — Сегодня понедельник.
    </div>
  </div>

  <div class="lesson-section">
    <h3>📆 Шаг 4. Месяцы</h3>
    <p>
      Месяцы тоже пишутся с маленькой буквы. Многие похожи на русские —
      запомнятся быстро.
    </p>

    <div class="lesson-cards">
      <div class="lesson-mini-card">
        <div class="mini-fr">janvier</div>
        <div class="mini-pron">жан-ВЬЕ</div>
        <div class="mini-ru">январь</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">février</div>
        <div class="mini-pron">фэв-РИ-Е</div>
        <div class="mini-ru">февраль</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">mars</div>
        <div class="mini-pron">марс</div>
        <div class="mini-ru">март</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">avril</div>
        <div class="mini-pron">а-ВРИЛЬ</div>
        <div class="mini-ru">апрель</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">mai</div>
        <div class="mini-pron">мэ</div>
        <div class="mini-ru">май</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">juin</div>
        <div class="mini-pron">жюэн</div>
        <div class="mini-ru">июнь</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">juillet</div>
        <div class="mini-pron">жюи-ЙЕ</div>
        <div class="mini-ru">июль</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">août</div>
        <div class="mini-pron">у</div>
        <div class="mini-ru">август</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">septembre</div>
        <div class="mini-pron">сэп-ТАНБР</div>
        <div class="mini-ru">сентябрь</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">octobre</div>
        <div class="mini-pron">ок-ТОБР</div>
        <div class="mini-ru">октябрь</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">novembre</div>
        <div class="mini-pron">но-ВАНБР</div>
        <div class="mini-ru">ноябрь</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">décembre</div>
        <div class="mini-pron">дэ-САНБР</div>
        <div class="mini-ru">декабрь</div>
      </div>
    </div>
  </div>

  <div class="lesson-section">
    <h3>🕐 Шаг 5. Время и полезные фразы</h3>
    <p>
      Чтобы спросить время, используй: <em>Quelle heure est-il ?</em>
      (Который час?). Ответ строится по схеме:
      <strong>Il est + число + heure(s)</strong>.
    </p>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Французский</th>
          <th>Звучит как</th>
          <th>Перевод</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>Quelle heure est-il ?</strong></td><td><em>кэль ёр э-ТИЛЬ</em></td><td>Который час?</td></tr>
        <tr><td><strong>Il est trois heures.</strong></td><td><em>иль э труа ЗЁР</em></td><td>Три часа.</td></tr>
        <tr><td><strong>Il est midi.</strong></td><td><em>иль э ми-ДИ</em></td><td>Полдень.</td></tr>
        <tr><td><strong>Il est minuit.</strong></td><td><em>иль э ми-НЮИ</em></td><td>Полночь.</td></tr>
        <tr><td><strong>du matin</strong></td><td><em>дю ма-ТЭН</em></td><td>утра</td></tr>
        <tr><td><strong>de l'après-midi</strong></td><td><em>дё ля-прэ-ми-ДИ</em></td><td>дня</td></tr>
        <tr><td><strong>du soir</strong></td><td><em>дю суар</em></td><td>вечера</td></tr>
      </tbody>
    </table>

    <p style="margin-top:18px;"><strong>Полезные слова времени:</strong></p>

    <div class="lesson-cards">
      <div class="lesson-mini-card">
        <div class="mini-fr">aujourd'hui</div>
        <div class="mini-pron">о-жур-ДЮИ</div>
        <div class="mini-ru">сегодня</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">demain</div>
        <div class="mini-pron">дё-МЭН</div>
        <div class="mini-ru">завтра</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">hier</div>
        <div class="mini-pron">йер</div>
        <div class="mini-ru">вчера</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">maintenant</div>
        <div class="mini-pron">мэн-тё-НАН</div>
        <div class="mini-ru">сейчас</div>
      </div>
    </div>

    <div class="lesson-mini-practice">
      <strong>🖊 Мини-практика:</strong>
      Скажи по-французски:
      <br>1) Сейчас 5 часов вечера → <em>Il est cinq heures du soir.</em>
      <br>2) Сегодня понедельник → <em>Aujourd'hui, c'est lundi.</em>
      <br>3) Завтра я еду в Париж → <em>Demain, je vais à Paris.</em>
    </div>
  </div>

  <!-- === КОНТРОЛЬНАЯ === -->
  <div class="lesson-quiz">
    <div class="quiz-head">
      <span class="quiz-badge">Контрольная</span>
      <h3>Собери предложения</h3>
      <p class="text-muted">Нажимай на кирпичики, чтобы построить перевод. Клик по выбранному слову — вернуть обратно.</p>
    </div>

    <div id="quiz-container-4"></div>

    <div class="quiz-finish hidden" id="quiz-finish-4">
      <span class="finish-emoji">🏆</span>
      <strong>Контрольная пройдена!</strong>
      <p id="quiz-score-4"></p>
    </div>
  </div>

  <div class="lesson-section" style="margin-top:32px;">
    <h3>📌 Что запомнить из урока 4</h3>
    <div class="lesson-cards">
      <div class="lesson-mini-card">
        <div class="mini-fr">un, deux, trois…</div>
        <div class="mini-pron">числа до 20</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">quatre-vingts</div>
        <div class="mini-pron">80 = 4 × 20</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">lundi, mardi…</div>
        <div class="mini-pron">дни недели</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">Il est trois heures</div>
        <div class="mini-pron">время</div>
      </div>
    </div>
  </div>

  <div class="lesson-finish">
    <span class="finish-emoji">🎉</span>
    <strong>Bravo !</strong>
    <p>Ты умеешь считать, называть дни и говорить о времени. Это огромный шаг. Дальше — вопросы и отрицания.</p>
  </div>

</div>

<script>
(function () {
    var container = document.getElementById('quiz-container-4');
    if (!container) return;

    var QUESTIONS = [
        {
            prompt: 'Переведи на французский',
            ru: 'Мне 20 лет',
            words: ['J\\'', 'ai', 'vingt', 'ans', 'suis', 'un'],
            answer: ['J\\'', 'ai', 'vingt', 'ans']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'Сейчас три часа',
            words: ['Il', 'est', 'trois', 'heures', 'sont', 'le'],
            answer: ['Il', 'est', 'trois', 'heures']
        },
        {
            prompt: 'Переведи на русский',
            ru: 'Aujourd\\'hui, c\\'est lundi',
            words: ['Сегодня', 'понедельник', 'вторник', 'завтра', 'среда'],
            answer: ['Сегодня', 'понедельник']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'Завтра я еду в Париж',
            words: ['Demain', 'je', 'vais', 'à', 'Paris', 'suis', 'le'],
            answer: ['Demain', 'je', 'vais', 'à', 'Paris']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'Восемьдесят три',
            words: ['quatre-vingt-trois', 'quatre-vingts', 'trois', 'huitante', 'quatre'],
            answer: ['quatre-vingt-trois']
        },
        {
            prompt: 'Переведи на русский',
            ru: 'Il est midi',
            words: ['Полдень', 'полночь', 'три', 'часа', 'вечер'],
            answer: ['Полдень']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'Который час?',
            words: ['Quelle', 'heure', 'est-il', 'est', 'quel', 'temps'],
            answer: ['Quelle', 'heure', 'est-il']
        }
    ];

    var current = 0;
    var correctCount = 0;

    function render() {
        if (current >= QUESTIONS.length) {
            showFinish();
            return;
        }

        var q = QUESTIONS[current];
        var html = '';

        html += '<div class="quiz-question">';
        html += '<div class="quiz-progress">Вопрос ' + (current + 1) + ' из ' + QUESTIONS.length + '</div>';
        html += '<div class="quiz-prompt">' + q.prompt + '</div>';
        html += '<div class="quiz-ru">«' + q.ru + '»</div>';
        html += '<div class="quiz-answer" id="quiz-answer-4" data-placeholder="Нажимай на кирпичики ниже"></div>';

        var shuffled = q.words.slice().sort(function () { return Math.random() - 0.5; });

        html += '<div class="quiz-words" id="quiz-words-4">';
        shuffled.forEach(function (w) {
            html += '<button type="button" class="quiz-word" data-word="' + w + '">' + w + '</button>';
        });
        html += '</div>';

        html += '<div class="quiz-actions">';
        html += '<button type="button" class="btn btn-ghost" id="quiz-skip-4">Пропустить</button>';
        html += '<button type="button" class="btn btn-primary" id="quiz-check-4" disabled>Проверить</button>';
        html += '</div>';

        html += '<div class="quiz-feedback hidden" id="quiz-feedback-4"></div>';
        html += '</div>';

        container.innerHTML = html;
        bindEvents();
    }

    function bindEvents() {
        var answerZone = document.getElementById('quiz-answer-4');
        var wordsZone = document.getElementById('quiz-words-4');
        var checkBtn = document.getElementById('quiz-check-4');
        var skipBtn = document.getElementById('quiz-skip-4');
        var feedback = document.getElementById('quiz-feedback-4');
        var q = QUESTIONS[current];

        function updateCheck() {
            var picked = answerZone.querySelectorAll('.quiz-word').length;
            checkBtn.disabled = picked === 0;
        }

        wordsZone.addEventListener('click', function (e) {
            var btn = e.target.closest('.quiz-word');
            if (!btn || btn.disabled) return;
            var clone = document.createElement('button');
            clone.type = 'button';
            clone.className = 'quiz-word quiz-word-picked';
            clone.setAttribute('data-word', btn.getAttribute('data-word'));
            clone.textContent = btn.textContent;
            answerZone.appendChild(clone);
            btn.style.visibility = 'hidden';
            btn.disabled = true;
            updateCheck();
        });

        answerZone.addEventListener('click', function (e) {
            var btn = e.target.closest('.quiz-word');
            if (!btn) return;
            var word = btn.getAttribute('data-word');
            var source = Array.from(wordsZone.querySelectorAll('.quiz-word'))
                .find(function (b) {
                    return b.getAttribute('data-word') === word && b.disabled;
                });
            if (source) {
                source.style.visibility = 'visible';
                source.disabled = false;
            }
            btn.remove();
            updateCheck();
        });

        checkBtn.addEventListener('click', function () {
            var picked = Array.from(answerZone.querySelectorAll('.quiz-word'))
                .map(function (b) { return b.getAttribute('data-word'); });

            var isCorrect = picked.length === q.answer.length &&
                picked.every(function (w, i) { return w === q.answer[i]; });

            if (isCorrect) {
                correctCount++;
                showFeedback(true, 'Правильно! 🎉');
            } else {
                showFeedback(false, 'Не совсем. Правильно: ' + q.answer.join(' '));
            }

            checkBtn.disabled = true;
            skipBtn.disabled = true;

            setTimeout(function () {
                current++;
                render();
            }, 1500);
        });

        skipBtn.addEventListener('click', function () {
            showFeedback(false, 'Правильный ответ: ' + q.answer.join(' '));
            checkBtn.disabled = true;
            skipBtn.disabled = true;
            setTimeout(function () {
                current++;
                render();
            }, 1500);
        });

        function showFeedback(ok, text) {
            feedback.textContent = text;
            feedback.className = 'quiz-feedback ' + (ok ? 'quiz-feedback-ok' : 'quiz-feedback-no');
        }
    }

    function showFinish() {
        container.classList.add('hidden');
        var finish = document.getElementById('quiz-finish-4');
        finish.classList.remove('hidden');
        var score = document.getElementById('quiz-score-4');
        score.textContent = 'Правильных ответов: ' + correctCount + ' из ' + QUESTIONS.length;
    }

    render();
})();
</script>
"""


LESSON_5_HTML = """
<div class="lesson-block">

  <div class="lesson-intro">
    <span class="lesson-chip">🇫🇷 Français · Débutant · Урок 5</span>
    <h2>Вопросы и отрицания</h2>
    <p class="lesson-lead">
      Ты уже умеешь строить утверждения. Теперь — самое важное для живого
      общения: <strong>задавать вопросы</strong> и <strong>говорить «нет»</strong>.
      Освоишь три способа задать вопрос и конструкцию <em>ne … pas</em>,
      которая делает предложение отрицательным. В конце — контрольная.
    </p>
  </div>

  <div class="lesson-goals">
    <h3>🎯 Что ты узнаешь</h3>
    <ul>
      <li>Три способа задать вопрос: интонацией, <em>est-ce que</em> и инверсией</li>
      <li>Вопросительные слова: кто, что, где, когда, почему, как</li>
      <li>Как построить отрицание: <em>ne … pas</em></li>
      <li>Особые формы: <em>ne … jamais</em>, <em>ne … plus</em>, <em>ne … rien</em></li>
      <li>Соберёшь вопросы и отрицания в интерактивной контрольной</li>
    </ul>
  </div>

  <div class="lesson-section">
    <h3>❓ Шаг 1. Три способа задать вопрос</h3>
    <p>
      Во французском можно спросить одно и то же <strong>тремя способами</strong>.
      Они отличаются по стилю: от разговорного до официального.
      Хорошая новость — тебя поймут в любом случае.
    </p>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Способ</th>
          <th>Пример</th>
          <th>Стиль</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>1. Интонация</strong></td>
          <td>Tu parles français ?</td>
          <td>Разговорный. Просто подними голос в конце.</td>
        </tr>
        <tr>
          <td><strong>2. Est-ce que</strong></td>
          <td>Est-ce que tu parles français ?</td>
          <td>Нейтральный. Работает всегда.</td>
        </tr>
        <tr>
          <td><strong>3. Инверсия</strong></td>
          <td>Parles-tu français ?</td>
          <td>Формальный / письменный.</td>
        </tr>
      </tbody>
    </table>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">💡</div>
      <div>
        <strong>Совет новичку:</strong> используй <em>est-ce que</em> —
        это универсальный способ. Он не требует менять порядок слов
        и подходит в любой ситуации. Просто ставишь <em>Est-ce que</em>
        в начало — и всё.
      </div>
    </div>

    <p style="margin-top:18px;"><strong>Как работает инверсия:</strong></p>
    <p>
      Глагол и местоимение меняются местами и соединяются дефисом:
    </p>
    <ul>
      <li><em>Tu es</em> → <em>Es-tu ?</em> (Ты есть? → Есть ли ты?)</li>
      <li><em>Il parle</em> → <em>Parle-t-il ?</em> (Он говорит?)</li>
      <li><em>Vous allez</em> → <em>Allez-vous ?</em> (Вы идёте?)</li>
    </ul>

    <div class="lesson-callout lesson-callout-warn">
      <div class="callout-icon">⚠️</div>
      <div>
        <strong>Хитрость:</strong> если глагол в 3-м лице заканчивается
        на гласную, добавляется <em>-t-</em> для благозвучия:
        <em>Parle-t-il ?</em>, <em>Va-t-elle ?</em>. Без этого было бы
        некрасиво: <s>Parle-il</s>.
      </div>
    </div>

    <div class="lesson-mini-practice">
      <strong>🖊 Мини-практика:</strong>
      Преврати утверждение в вопрос тремя способами:
      <br><em>Tu aimes le café.</em> (Ты любишь кофе.)
      <br>1) <em>Tu aimes le café ?</em>
      <br>2) <em>Est-ce que tu aimes le café ?</em>
      <br>3) <em>Aimes-tu le café ?</em>
    </div>
  </div>

  <div class="lesson-section">
    <h3>🔍 Шаг 2. Вопросительные слова</h3>
    <p>
      Чтобы задать содержательный вопрос, нужны вопросительные слова.
      Они ставятся в начало предложения — как в русском.
    </p>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Французский</th>
          <th>Звучит как</th>
          <th>Перевод</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>Qui ?</strong></td><td><em>ки</em></td><td>Кто?</td></tr>
        <tr><td><strong>Que ? / Qu'est-ce que ?</strong></td><td><em>кё / кэс-кё</em></td><td>Что?</td></tr>
        <tr><td><strong>Où ?</strong></td><td><em>у</em></td><td>Где? / Куда?</td></tr>
        <tr><td><strong>Quand ?</strong></td><td><em>кан</em></td><td>Когда?</td></tr>
        <tr><td><strong>Pourquoi ?</strong></td><td><em>пур-КУА</em></td><td>Почему?</td></tr>
        <tr><td><strong>Comment ?</strong></td><td><em>ко-МАН</em></td><td>Как?</td></tr>
        <tr><td><strong>Combien ?</strong></td><td><em>ком-БЬЕН</em></td><td>Сколько?</td></tr>
      </tbody>
    </table>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">💡</div>
      <div>
        <strong>Qu'est-ce que</strong> — это «что» в значении «что именно».
        <em>Qu'est-ce que tu fais ?</em> = «Что ты делаешь?».
        А просто <em>Que</em> используется в формальном стиле:
        <em>Que fais-tu ?</em> — то же самое, но книжно.
      </div>
    </div>

    <p style="margin-top:18px;"><strong>Примеры вопросов:</strong></p>

    <div class="lesson-examples">
      <div class="example-row">
        <div class="example-fr">Où habites-tu ?</div>
        <div class="example-ru">Где ты живёшь?</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Quand vas-tu à Paris ?</div>
        <div class="example-ru">Когда ты едешь в Париж?</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Pourquoi tu apprends le français ?</div>
        <div class="example-ru">Почему ты учишь французский?</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Comment tu t'appelles ?</div>
        <div class="example-ru">Как тебя зовут?</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Combien ça coûte ?</div>
        <div class="example-ru">Сколько это стоит?</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Qui est-ce ?</div>
        <div class="example-ru">Кто это?</div>
      </div>
    </div>

    <div class="lesson-mini-practice">
      <strong>🖊 Мини-практика:</strong>
      Задай вопрос к выделенному слову:
      <br>1) <em>Je vais <strong>à Paris</strong>.</em> → <em>Où vas-tu ?</em>
      <br>2) <em>Je pars <strong>demain</strong>.</em> → <em>Quand pars-tu ?</em>
      <br>3) <em>J'apprends le français <strong>pour travailler</strong>.</em> → <em>Pourquoi apprends-tu le français ?</em>
    </div>
  </div>

  <div class="lesson-section">
    <h3>🚫 Шаг 3. Отрицание: ne … pas</h3>
    <p>
      Чтобы сказать «не», во французском используется <strong>двойное
      отрицание</strong>: <em>ne</em> перед глаголом и <em>pas</em> после него.
      Как в русском «не хочу» — только «не» стоит с двух сторон.
    </p>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">🧩</div>
      <div style="text-align:center; font-size: 1.05rem;">
        <strong>Подлежащее + ne + глагол + pas + дополнение</strong><br>
        <em>Je</em> + <em>ne</em> + <em>parle</em> + <em>pas</em> + <em>français</em><br>
        Я не говорю по-французски.
      </div>
    </div>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Утверждение</th>
          <th>Отрицание</th>
          <th>Перевод</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Je parle français.</td>
          <td><strong>Je ne parle pas français.</strong></td>
          <td>Я не говорю по-французски.</td>
        </tr>
        <tr>
          <td>Tu es étudiant.</td>
          <td><strong>Tu n'es pas étudiant.</strong></td>
          <td>Ты не студент.</td>
        </tr>
        <tr>
          <td>Il a un chat.</td>
          <td><strong>Il n'a pas de chat.</strong></td>
          <td>У него нет кота.</td>
        </tr>
        <tr>
          <td>Nous allons à Paris.</td>
          <td><strong>Nous n'allons pas à Paris.</strong></td>
          <td>Мы не едем в Париж.</td>
        </tr>
        <tr>
          <td>Elles aiment le café.</td>
          <td><strong>Elles n'aiment pas le café.</strong></td>
          <td>Они не любят кофе.</td>
        </tr>
      </tbody>
    </table>

    <div class="lesson-callout lesson-callout-warn">
      <div class="callout-icon">⚠️</div>
      <div>
        <strong>Элизия:</strong> <em>ne</em> перед гласной или немой h
        превращается в <em>n'</em>: <em>n'es pas</em>, <em>n'a pas</em>,
        <em>n'habite pas</em>. Это обязательно!
      </div>
    </div>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">🇷🇺</div>
      <div>
        <strong>Важно:</strong> после <em>pas</em> неопределённый артикль
        <em>un / une / des</em> обычно заменяется на <em>de</em>:
        <em>J'ai un chat</em> → <em>Je n'ai pas <strong>de</strong> chat</em>.
        Но определённый артикль <em>le / la / les</em> остаётся:
        <em>Je n'aime pas <strong>le</strong> café</em>.
      </div>
    </div>

    <div class="lesson-mini-practice">
      <strong>🖊 Мини-практика:</strong>
      Сделай предложения отрицательными:
      <br>1) <em>Je suis russe.</em> → <em>Je ne suis pas russe.</em>
      <br>2) <em>Il habite à Moscou.</em> → <em>Il n'habite pas à Moscou.</em>
      <br>3) <em>Nous avons un chien.</em> → <em>Nous n'avons pas de chien.</em>
    </div>
  </div>

  <div class="lesson-section">
    <h3>🚫 Шаг 4. Другие отрицания</h3>
    <p>
      <em>Pas</em> — не единственное отрицание. Есть ещё несколько,
      которые работают по той же схеме: <em>ne</em> + глагол + второе слово.
    </p>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Отрицание</th>
          <th>Перевод</th>
          <th>Пример</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>ne … pas</strong></td>
          <td>не</td>
          <td>Je ne parle pas. — Я не говорю.</td>
        </tr>
        <tr>
          <td><strong>ne … jamais</strong></td>
          <td>никогда не</td>
          <td>Je ne fume jamais. — Я никогда не курю.</td>
        </tr>
        <tr>
          <td><strong>ne … plus</strong></td>
          <td>больше не</td>
          <td>Il ne travaille plus. — Он больше не работает.</td>
        </tr>
        <tr>
          <td><strong>ne … rien</strong></td>
          <td>ничего не</td>
          <td>Je ne sais rien. — Я ничего не знаю.</td>
        </tr>
        <tr>
          <td><strong>ne … personne</strong></td>
          <td>никого не</td>
          <td>Je ne vois personne. — Я никого не вижу.</td>
        </tr>
      </tbody>
    </table>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">💡</div>
      <div>
        <strong>Запомни:</strong> <em>jamais</em>, <em>plus</em>, <em>rien</em>,
        <em>personne</em> ставятся на то же место, что и <em>pas</em> —
        после глагола. Схема всегда одна: <em>ne + глагол + второе слово</em>.
      </div>
    </div>

    <div class="lesson-callout lesson-callout-warn">
      <div class="callout-icon">⚠️</div>
      <div>
        <strong>В разговорной речи</strong> французы часто опускают
        <em>ne</em>: <em>Je parle pas</em>, <em>Je sais pas</em>.
        Это нормально в неформальном общении, но на письме и в официальной
        речи <em>ne</em> обязательно.
      </div>
    </div>

    <div class="lesson-mini-practice">
      <strong>🖊 Мини-практика:</strong>
      Переведи на французский:
      <br>1) Я никогда не ем мясо → <em>Je ne mange jamais de viande.</em>
      <br>2) Она больше не живёт здесь → <em>Elle n'habite plus ici.</em>
      <br>3) Мы ничего не видим → <em>Nous ne voyons rien.</em>
    </div>
  </div>

  <div class="lesson-section">
    <h3>💬 Шаг 5. Вопрос + отрицание</h3>
    <p>
      Теперь ты можешь комбинировать: задавать вопрос в отрицательной форме.
      Например: <em>Tu ne parles pas français ?</em> — «Ты не говоришь
      по-французски?». Порядок слов такой:
    </p>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">🧩</div>
      <div style="text-align:center; font-size: 1.05rem;">
        <strong>Est-ce que + подлежащее + ne + глагол + pas ?</strong><br>
        <em>Est-ce que tu ne parles pas français ?</em>
      </div>
    </div>

    <div class="lesson-examples">
      <div class="example-row">
        <div class="example-fr">Est-ce que tu ne comprends pas ?</div>
        <div class="example-ru">Ты не понимаешь?</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Pourquoi tu ne manges pas ?</div>
        <div class="example-ru">Почему ты не ешь?</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Il ne vient pas aujourd'hui ?</div>
        <div class="example-ru">Он не приходит сегодня?</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Vous n'avez pas de question ?</div>
        <div class="example-ru">У вас нет вопросов?</div>
      </div>
    </div>
  </div>

  <!-- === КОНТРОЛЬНАЯ === -->
  <div class="lesson-quiz">
    <div class="quiz-head">
      <span class="quiz-badge">Контрольная</span>
      <h3>Собери предложения</h3>
      <p class="text-muted">Нажимай на кирпичики, чтобы построить перевод. Клик по выбранному слову — вернуть обратно.</p>
    </div>

    <div id="quiz-container-5"></div>

    <div class="quiz-finish hidden" id="quiz-finish-5">
      <span class="finish-emoji">🏆</span>
      <strong>Контрольная пройдена!</strong>
      <p id="quiz-score-5"></p>
    </div>
  </div>

  <div class="lesson-section" style="margin-top:32px;">
    <h3>📌 Что запомнить из урока 5</h3>
    <div class="lesson-cards">
      <div class="lesson-mini-card">
        <div class="mini-fr">Est-ce que…</div>
        <div class="mini-pron">универсальный вопрос</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">Où, quand, pourquoi…</div>
        <div class="mini-pron">вопросительные слова</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">ne … pas</div>
        <div class="mini-pron">отрицание</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">ne … jamais</div>
        <div class="mini-pron">никогда не</div>
      </div>
    </div>
  </div>

  <div class="lesson-finish">
    <span class="finish-emoji">🎉</span>
    <strong>Félicitations !</strong>
    <p>Ты научился задавать вопросы и говорить «нет». Это открывает настоящий диалог. Дальше — прошедшее время и будущее.</p>
  </div>

</div>

<script>
(function () {
    var container = document.getElementById('quiz-container-5');
    if (!container) return;

    var QUESTIONS = [
        {
            prompt: 'Переведи на французский',
            ru: 'Ты говоришь по-французски? (est-ce que)',
            words: ['Est-ce', 'que', 'tu', 'parles', 'français', 'es', 'le'],
            answer: ['Est-ce', 'que', 'tu', 'parles', 'français']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'Я не говорю по-французски',
            words: ['Je', 'ne', 'parle', 'pas', 'français', 'suis', 'le'],
            answer: ['Je', 'ne', 'parle', 'pas', 'français']
        },
        {
            prompt: 'Переведи на русский',
            ru: 'Où habites-tu ?',
            words: ['Где', 'ты', 'живёшь', 'Когда', 'едешь', 'Париж'],
            answer: ['Где', 'ты', 'живёшь']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'Почему ты не ешь?',
            words: ['Pourquoi', 'tu', 'ne', 'manges', 'pas', 'est', 'le'],
            answer: ['Pourquoi', 'tu', 'ne', 'manges', 'pas']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'Я никогда не курю',
            words: ['Je', 'ne', 'fume', 'jamais', 'pas', 'suis'],
            answer: ['Je', 'ne', 'fume', 'jamais']
        },
        {
            prompt: 'Переведи на русский',
            ru: 'Il ne travaille plus',
            words: ['Он', 'больше', 'не', 'работает', 'никогда', 'живёт'],
            answer: ['Он', 'больше', 'не', 'работает']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'Сколько это стоит?',
            words: ['Combien', 'ça', 'coûte', 'est', 'que', 'le'],
            answer: ['Combien', 'ça', 'coûte']
        }
    ];

    var current = 0;
    var correctCount = 0;

    function render() {
        if (current >= QUESTIONS.length) {
            showFinish();
            return;
        }

        var q = QUESTIONS[current];
        var html = '';

        html += '<div class="quiz-question">';
        html += '<div class="quiz-progress">Вопрос ' + (current + 1) + ' из ' + QUESTIONS.length + '</div>';
        html += '<div class="quiz-prompt">' + q.prompt + '</div>';
        html += '<div class="quiz-ru">«' + q.ru + '»</div>';
        html += '<div class="quiz-answer" id="quiz-answer-5" data-placeholder="Нажимай на кирпичики ниже"></div>';

        var shuffled = q.words.slice().sort(function () { return Math.random() - 0.5; });

        html += '<div class="quiz-words" id="quiz-words-5">';
        shuffled.forEach(function (w) {
            html += '<button type="button" class="quiz-word" data-word="' + w + '">' + w + '</button>';
        });
        html += '</div>';

        html += '<div class="quiz-actions">';
        html += '<button type="button" class="btn btn-ghost" id="quiz-skip-5">Пропустить</button>';
        html += '<button type="button" class="btn btn-primary" id="quiz-check-5" disabled>Проверить</button>';
        html += '</div>';

        html += '<div class="quiz-feedback hidden" id="quiz-feedback-5"></div>';
        html += '</div>';

        container.innerHTML = html;
        bindEvents();
    }

    function bindEvents() {
        var answerZone = document.getElementById('quiz-answer-5');
        var wordsZone = document.getElementById('quiz-words-5');
        var checkBtn = document.getElementById('quiz-check-5');
        var skipBtn = document.getElementById('quiz-skip-5');
        var feedback = document.getElementById('quiz-feedback-5');
        var q = QUESTIONS[current];

        function updateCheck() {
            var picked = answerZone.querySelectorAll('.quiz-word').length;
            checkBtn.disabled = picked === 0;
        }

        wordsZone.addEventListener('click', function (e) {
            var btn = e.target.closest('.quiz-word');
            if (!btn || btn.disabled) return;
            var clone = document.createElement('button');
            clone.type = 'button';
            clone.className = 'quiz-word quiz-word-picked';
            clone.setAttribute('data-word', btn.getAttribute('data-word'));
            clone.textContent = btn.textContent;
            answerZone.appendChild(clone);
            btn.style.visibility = 'hidden';
            btn.disabled = true;
            updateCheck();
        });

        answerZone.addEventListener('click', function (e) {
            var btn = e.target.closest('.quiz-word');
            if (!btn) return;
            var word = btn.getAttribute('data-word');
            var source = Array.from(wordsZone.querySelectorAll('.quiz-word'))
                .find(function (b) {
                    return b.getAttribute('data-word') === word && b.disabled;
                });
            if (source) {
                source.style.visibility = 'visible';
                source.disabled = false;
            }
            btn.remove();
            updateCheck();
        });

        checkBtn.addEventListener('click', function () {
            var picked = Array.from(answerZone.querySelectorAll('.quiz-word'))
                .map(function (b) { return b.getAttribute('data-word'); });

            var isCorrect = picked.length === q.answer.length &&
                picked.every(function (w, i) { return w === q.answer[i]; });

            if (isCorrect) {
                correctCount++;
                showFeedback(true, 'Правильно! 🎉');
            } else {
                showFeedback(false, 'Не совсем. Правильно: ' + q.answer.join(' '));
            }

            checkBtn.disabled = true;
            skipBtn.disabled = true;

            setTimeout(function () {
                current++;
                render();
            }, 1500);
        });

        skipBtn.addEventListener('click', function () {
            showFeedback(false, 'Правильный ответ: ' + q.answer.join(' '));
            checkBtn.disabled = true;
            skipBtn.disabled = true;
            setTimeout(function () {
                current++;
                render();
            }, 1500);
        });

        function showFeedback(ok, text) {
            feedback.textContent = text;
            feedback.className = 'quiz-feedback ' + (ok ? 'quiz-feedback-ok' : 'quiz-feedback-no');
        }
    }

    function showFinish() {
        container.classList.add('hidden');
        var finish = document.getElementById('quiz-finish-5');
        finish.classList.remove('hidden');
        var score = document.getElementById('quiz-score-5');
        score.textContent = 'Правильных ответов: ' + correctCount + ' из ' + QUESTIONS.length;
    }

    render();
})();
</script>
"""

# =====================================================================
# УРОК 6 — ГЛАГОЛЫ ВТОРОЙ ГРУППЫ И ПРОШЕДШЕЕ ВРЕМЯ
# =====================================================================

LESSON_6_HTML = """
<div class="lesson-block">

  <div class="lesson-intro">
    <span class="lesson-chip">🇫🇷 Français · Élémentaire · Урок 6</span>
    <h2>Passé composé — прошедшее время</h2>
    <p class="lesson-lead">
      Ты уже умеешь говорить о настоящем. Теперь — <strong>прошедшее
      время</strong> (passé composé). Это самое частое прошедшее
      во французском. Ты узнаешь, как образуются формы с <em>avoir</em>
      и <em>être</em>, и почему некоторые глаголы «идут не по правилам».
      В конце — контрольная.
    </p>
  </div>

  <div class="lesson-goals">
    <h3>🎯 Что ты узнаешь</h3>
    <ul>
      <li>Что такое passé composé и когда его использовать</li>
      <li>Причастия прошедшего времени (participe passé)</li>
      <li>Спряжение с <em>avoir</em> — большинство глаголов</li>
      <li>Спряжение с <em>être</em> — «движение и состояние»</li>
      <li>Согласование причастия с подлежащим</li>
    </ul>
  </div>

  <div class="lesson-section">
    <h3>📅 Шаг 1. Что такое passé composé</h3>
    <p>
      <strong>Passé composé</strong> — сложное прошедшее время.
      Оно используется для <strong>завершённых действий</strong>:
      «я сделал», «он пришёл», «мы поели».
    </p>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">🧩</div>
      <div style="text-align:center; font-size: 1.05rem;">
        <strong>Passé composé = вспомогательный глагол + причастие</strong><br>
        <em>J'ai parlé</em> — Я поговорил<br>
        <em>Je suis allé</em> — Я пошёл
      </div>
    </div>

    <p style="margin-top:18px;">
      Вспомогательный глагол — это <em>avoir</em> (иметь) или
      <em>être</em> (быть) в настоящем времени. Причастие — это
      «сделанная» форма глагола.
    </p>
  </div>

  <div class="lesson-section">
    <h3>🔤 Шаг 2. Participe passé — причастие</h3>
    <p>
      У правильных глаголов причастие образуется просто:
    </p>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Группа</th>
          <th>Правило</th>
          <th>Пример</th>
          <th>Перевод</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>-er</strong></td>
          <td>-er → <strong>-é</strong></td>
          <td>parler → parl<strong>é</strong></td>
          <td>говорить → поговорил</td>
        </tr>
        <tr>
          <td><strong>-ir</strong></td>
          <td>-ir → <strong>-i</strong></td>
          <td>finir → fin<strong>i</strong></td>
          <td>заканчивать → закончил</td>
        </tr>
        <tr>
          <td><strong>-re</strong></td>
          <td>-re → <strong>-u</strong></td>
          <td>vendre → vend<strong>u</strong></td>
          <td>продавать → продал</td>
        </tr>
      </tbody>
    </table>

    <p style="margin-top:18px;"><strong>Неправильные причастия (надо выучить):</strong></p>

    <div class="lesson-cards">
      <div class="lesson-mini-card">
        <div class="mini-fr">avoir → eu</div>
        <div class="mini-pron">а-ВУАР → ю</div>
        <div class="mini-ru">иметь → имел</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">être → été</div>
        <div class="mini-pron">этр → э-ТЭ</div>
        <div class="mini-ru">быть → был</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">faire → fait</div>
        <div class="mini-pron">фэр → фэ</div>
        <div class="mini-ru">делать → сделал</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">voir → vu</div>
        <div class="mini-pron">вуар → вю</div>
        <div class="mini-ru">видеть → увидел</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">prendre → pris</div>
        <div class="mini-pron">прандр → при</div>
        <div class="mini-ru">брать → взял</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">dire → dit</div>
        <div class="mini-pron">дир → ди</div>
        <div class="mini-ru">говорить → сказал</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">écrire → écrit</div>
        <div class="mini-pron">экрир → эк-РИ</div>
        <div class="mini-ru">писать → написал</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">lire → lu</div>
        <div class="mini-pron">лир → лю</div>
        <div class="mini-ru">читать → прочитал</div>
      </div>
    </div>
  </div>

  <div class="lesson-section">
    <h3>🅰️ Шаг 3. Спряжение с avoir</h3>
    <p>
      <strong>Большинство глаголов</strong> спрягаются с <em>avoir</em>.
      Схема: подлежащее + avoir в настоящем + причастие.
    </p>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Местоимение</th>
          <th>Форма parler</th>
          <th>Перевод</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>j'</td><td><strong>ai parlé</strong></td><td>я поговорил</td></tr>
        <tr><td>tu</td><td><strong>as parlé</strong></td><td>ты поговорил</td></tr>
        <tr><td>il / elle</td><td><strong>a parlé</strong></td><td>он / она поговорил(а)</td></tr>
        <tr><td>nous</td><td><strong>avons parlé</strong></td><td>мы поговорили</td></tr>
        <tr><td>vous</td><td><strong>avez parlé</strong></td><td>вы поговорили</td></tr>
        <tr><td>ils / elles</td><td><strong>ont parlé</strong></td><td>они поговорили</td></tr>
      </tbody>
    </table>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">💡</div>
      <div>
        <strong>С avoir</strong> причастие <strong>не согласуется</strong>
        с подлежащим: <em>Elle a parlé</em> (она поговорила) — не
        «parlée». Пишется одинаковая форма для всех.
      </div>
    </div>
  </div>

  <div class="lesson-section">
    <h3>🅱️ Шаг 4. Спряжение с être</h3>
    <p>
      Некоторые глаголы спрягаются с <em>être</em>. Это в основном
      глаголы <strong>движения и изменения состояния</strong>.
      Их надо запомнить — их около 14.
    </p>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Глагол</th>
          <th>Перевод</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>aller</strong></td><td>идти</td></tr>
        <tr><td><strong>venir</strong></td><td>приходить</td></tr>
        <tr><td><strong>arriver</strong></td><td>прибывать</td></tr>
        <tr><td><strong>partir</strong></td><td>уезжать</td></tr>
        <tr><td><strong>entrer</strong></td><td>входить</td></tr>
        <tr><td><strong>sortir</strong></td><td>выходить</td></tr>
        <tr><td><strong>naître</strong></td><td>рождаться</td></tr>
        <tr><td><strong>mourir</strong></td><td>умирать</td></tr>
        <tr><td><strong>rester</strong></td><td>оставаться</td></tr>
        <tr><td><strong>tomber</strong></td><td>падать</td></tr>
        <tr><td><strong>monter</strong></td><td>подниматься</td></tr>
        <tr><td><strong>descendre</strong></td><td>спускаться</td></tr>
        <tr><td><strong>devenir</strong></td><td>становиться</td></tr>
        <tr><td><strong>retourner</strong></td><td>возвращаться</td></tr>
      </tbody>
    </table>

    <p style="margin-top:18px;"><strong>Спряжение aller:</strong></p>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Местоимение</th>
          <th>Форма</th>
          <th>Перевод</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>je</td><td><strong>suis allé(e)</strong></td><td>я пошёл / пошла</td></tr>
        <tr><td>tu</td><td><strong>es allé(e)</strong></td><td>ты пошёл / пошла</td></tr>
        <tr><td>il</td><td><strong>est allé</strong></td><td>он пошёл</td></tr>
        <tr><td>elle</td><td><strong>est allée</strong></td><td>она пошла</td></tr>
        <tr><td>nous</td><td><strong>sommes allé(e)s</strong></td><td>мы пошли</td></tr>
        <tr><td>vous</td><td><strong>êtes allé(e)(s)</strong></td><td>вы пошли</td></tr>
        <tr><td>ils</td><td><strong>sont allés</strong></td><td>они пошли (м.)</td></tr>
        <tr><td>elles</td><td><strong>sont allées</strong></td><td>они пошли (ж.)</td></tr>
      </tbody>
    </table>

    <div class="lesson-callout lesson-callout-warn">
      <div class="callout-icon">⚠️</div>
      <div>
        <strong>С être</strong> причастие <strong>согласуется</strong>
        с подлежащим в роде и числе: женщина добавляет <em>-e</em>,
        множественное число — <em>-s</em>. <em>Elle est allée</em>,
        <em>Ils sont allés</em>.
      </div>
    </div>

    <div class="lesson-mini-practice">
      <strong>🖊 Мини-практика:</strong>
      Поставь в passé composé:
      <br>1) Je (parler) français. → <em>J'ai parlé français.</em>
      <br>2) Elle (aller) à Paris. → <em>Elle est allée à Paris.</em>
      <br>3) Nous (manger) une pizza. → <em>Nous avons mangé une pizza.</em>
      <br>4) Ils (venir) hier. → <em>Ils sont venus hier.</em>
    </div>
  </div>

  <div class="lesson-section">
    <h3>💬 Шаг 5. Отрицание и вопросы</h3>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">🧩</div>
      <div>
        <strong>Отрицание:</strong> ne + avoir/être + pas + причастие<br>
        <em>Je <strong>n'ai pas</strong> parlé.</em> — Я не поговорил.<br>
        <em>Elle <strong>n'est pas</strong> allée.</em> — Она не пошла.<br><br>
        <strong>Вопрос (инверсия):</strong><br>
        <em><strong>As-tu</strong> parlé ?</em> — Ты поговорил?<br>
        <em><strong>Est-elle</strong> allée ?</em> — Она пошла?
      </div>
    </div>

    <div class="lesson-examples">
      <div class="example-row">
        <div class="example-fr">J'ai mangé au restaurant.</div>
        <div class="example-ru">Я поел в ресторане.</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Elle est arrivée hier.</div>
        <div class="example-ru">Она приехала вчера.</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Nous n'avons pas vu le film.</div>
        <div class="example-ru">Мы не видели фильм.</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Ils sont partis à midi.</div>
        <div class="example-ru">Они уехали в полдень.</div>
      </div>
    </div>
  </div>

  <!-- === КОНТРОЛЬНАЯ === -->
  <div class="lesson-quiz">
    <div class="quiz-head">
      <span class="quiz-badge">Контрольная</span>
      <h3>Собери предложения</h3>
      <p class="text-muted">Нажимай на кирпичики, чтобы построить перевод. Клик по выбранному слову — вернуть обратно.</p>
    </div>

    <div id="quiz-container-6"></div>

    <div class="quiz-finish hidden" id="quiz-finish-6">
      <span class="finish-emoji">🏆</span>
      <strong>Контрольная пройдена!</strong>
      <p id="quiz-score-6"></p>
    </div>
  </div>

  <div class="lesson-section" style="margin-top:32px;">
    <h3>📌 Что запомнить из урока 6</h3>
    <div class="lesson-cards">
      <div class="lesson-mini-card">
        <div class="mini-fr">j'ai parlé</div>
        <div class="mini-pron">passé composé с avoir</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">je suis allé(e)</div>
        <div class="mini-pron">passé composé с être</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">-é, -i, -u</div>
        <div class="mini-pron">причастия</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">ne … pas</div>
        <div class="mini-pron">отрицание</div>
      </div>
    </div>
  </div>

  <div class="lesson-task">
    <div class="task-head">
      <span class="task-badge">Практика</span>
      <h3>Закрепи материал</h3>
    </div>
    <ol>
      <li>Поставь в passé composé: <em>Je (manger) une pomme.</em></li>
      <li>Поставь в passé composé: <em>Elle (aller) à Paris.</em></li>
      <li>Сделай отрицание: <em>J'ai vu ce film.</em></li>
      <li>Переведи: «Мы приехали вчера».</li>
    </ol>
    <p class="task-hint">
      Подсказка: <em>J'ai mangé une pomme · Elle est allée à Paris ·
      Je n'ai pas vu ce film · Nous sommes arrivés hier</em>
    </p>
  </div>

  <div class="lesson-finish">
    <span class="finish-emoji">🎉</span>
    <strong>Félicitations !</strong>
    <p>Ты умеешь говорить о прошлом. Дальше — будущее время.</p>
  </div>

</div>

<script>
(function () {
    var container = document.getElementById('quiz-container-6');
    if (!container) return;

    var QUESTIONS = [
        {
            prompt: 'Переведи на французский',
            ru: 'Я поел',
            words: ['J\\'', 'ai', 'mangé', 'suis', 'le'],
            answer: ['J\\'', 'ai', 'mangé']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'Она пошла в Париж',
            words: ['Elle', 'est', 'allée', 'à', 'Paris', 'a'],
            answer: ['Elle', 'est', 'allée', 'à', 'Paris']
        },
        {
            prompt: 'Переведи на русский',
            ru: 'Nous avons vu le film',
            words: ['Мы', 'видели', 'фильм', 'ели', 'шли'],
            answer: ['Мы', 'видели', 'фильм']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'Они приехали вчера',
            words: ['Ils', 'sont', 'arrivés', 'hier', 'ont', 'le'],
            answer: ['Ils', 'sont', 'arrivés', 'hier']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'Я не говорил по-французски',
            words: ['Je', 'n\\'', 'ai', 'pas', 'parlé', 'français', 'suis'],
            answer: ['Je', 'n\\'', 'ai', 'pas', 'parlé', 'français']
        },
        {
            prompt: 'Переведи на русский',
            ru: 'Elle est partie',
            words: ['Она', 'уехала', 'пришла', 'видела', 'ела'],
            answer: ['Она', 'уехала']
        }
    ];

    var current = 0;
    var correctCount = 0;

    function render() {
        if (current >= QUESTIONS.length) {
            showFinish();
            return;
        }

        var q = QUESTIONS[current];
        var html = '';

        html += '<div class="quiz-question">';
        html += '<div class="quiz-progress">Вопрос ' + (current + 1) + ' из ' + QUESTIONS.length + '</div>';
        html += '<div class="quiz-prompt">' + q.prompt + '</div>';
        html += '<div class="quiz-ru">«' + q.ru + '»</div>';
        html += '<div class="quiz-answer" id="quiz-answer-6" data-placeholder="Нажимай на кирпичики ниже"></div>';

        var shuffled = q.words.slice().sort(function () { return Math.random() - 0.5; });

        html += '<div class="quiz-words" id="quiz-words-6">';
        shuffled.forEach(function (w) {
            html += '<button type="button" class="quiz-word" data-word="' + w + '">' + w + '</button>';
        });
        html += '</div>';

        html += '<div class="quiz-actions">';
        html += '<button type="button" class="btn btn-ghost" id="quiz-skip-6">Пропустить</button>';
        html += '<button type="button" class="btn btn-primary" id="quiz-check-6" disabled>Проверить</button>';
        html += '</div>';

        html += '<div class="quiz-feedback hidden" id="quiz-feedback-6"></div>';
        html += '</div>';

        container.innerHTML = html;
        bindEvents();
    }

    function bindEvents() {
        var answerZone = document.getElementById('quiz-answer-6');
        var wordsZone = document.getElementById('quiz-words-6');
        var checkBtn = document.getElementById('quiz-check-6');
        var skipBtn = document.getElementById('quiz-skip-6');
        var feedback = document.getElementById('quiz-feedback-6');
        var q = QUESTIONS[current];

        function updateCheck() {
            var picked = answerZone.querySelectorAll('.quiz-word').length;
            checkBtn.disabled = picked === 0;
        }

        wordsZone.addEventListener('click', function (e) {
            var btn = e.target.closest('.quiz-word');
            if (!btn || btn.disabled) return;
            var clone = document.createElement('button');
            clone.type = 'button';
            clone.className = 'quiz-word quiz-word-picked';
            clone.setAttribute('data-word', btn.getAttribute('data-word'));
            clone.textContent = btn.textContent;
            answerZone.appendChild(clone);
            btn.style.visibility = 'hidden';
            btn.disabled = true;
            updateCheck();
        });

        answerZone.addEventListener('click', function (e) {
            var btn = e.target.closest('.quiz-word');
            if (!btn) return;
            var word = btn.getAttribute('data-word');
            var source = Array.from(wordsZone.querySelectorAll('.quiz-word'))
                .find(function (b) {
                    return b.getAttribute('data-word') === word && b.disabled;
                });
            if (source) {
                source.style.visibility = 'visible';
                source.disabled = false;
            }
            btn.remove();
            updateCheck();
        });

        checkBtn.addEventListener('click', function () {
            var picked = Array.from(answerZone.querySelectorAll('.quiz-word'))
                .map(function (b) { return b.getAttribute('data-word'); });

            var isCorrect = picked.length === q.answer.length &&
                picked.every(function (w, i) { return w === q.answer[i]; });

            if (isCorrect) {
                correctCount++;
                showFeedback(true, 'Правильно! 🎉');
            } else {
                showFeedback(false, 'Не совсем. Правильно: ' + q.answer.join(' '));
            }

            checkBtn.disabled = true;
            skipBtn.disabled = true;

            setTimeout(function () {
                current++;
                render();
            }, 1500);
        });

        skipBtn.addEventListener('click', function () {
            showFeedback(false, 'Правильный ответ: ' + q.answer.join(' '));
            checkBtn.disabled = true;
            skipBtn.disabled = true;
            setTimeout(function () {
                current++;
                render();
            }, 1500);
        });

        function showFeedback(ok, text) {
            feedback.textContent = text;
            feedback.className = 'quiz-feedback ' + (ok ? 'quiz-feedback-ok' : 'quiz-feedback-no');
        }
    }

    function showFinish() {
        container.classList.add('hidden');
        var finish = document.getElementById('quiz-finish-6');
        finish.classList.remove('hidden');
        var score = document.getElementById('quiz-score-6');
        score.textContent = 'Правильных ответов: ' + correctCount + ' из ' + QUESTIONS.length;
    }

    render();
})();
</script>
"""


# =====================================================================
# УРОК 7 — БУДУЩЕЕ ВРЕМЯ
# =====================================================================

LESSON_7_HTML = """
<div class="lesson-block">

  <div class="lesson-intro">
    <span class="lesson-chip">🇫🇷 Français · Élémentaire · Урок 7</span>
    <h2>Futur — будущее время</h2>
    <p class="lesson-lead">
      Прошлое ты знаешь. Осталось будущее. Во французском есть
      <strong>два будущих</strong>: ближайшее (<em>futur proche</em>) —
      «я собираюсь сделать» — и простое (<em>futur simple</em>) —
      «я сделаю». Ты узнаешь оба и поймёшь, когда какое использовать.
    </p>
  </div>

  <div class="lesson-goals">
    <h3>🎯 Что ты узнаешь</h3>
    <ul>
      <li>Futur proche — ближайшее будущее с <em>aller</em></li>
      <li>Futur simple — простое будущее</li>
      <li>Неправильные формы: être, avoir, aller, faire…</li>
      <li>Разница между двумя будущими</li>
      <li>Маркеры времени: demain, la semaine prochaine, bientôt</li>
    </ul>
  </div>

  <div class="lesson-section">
    <h3>🚀 Шаг 1. Futur proche — ближайшее будущее</h3>
    <p>
      Самое простое будущее. Схема: <strong>aller в настоящем +
      инфинитив</strong>. Как в русском «я иду делать», «я собираюсь».
    </p>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">🧩</div>
      <div style="text-align:center; font-size: 1.05rem;">
        <strong>aller + инфинитив</strong><br>
        <em>Je vais parler</em> — Я собираюсь поговорить<br>
        <em>Nous allons manger</em> — Мы сейчас поедим
      </div>
    </div>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Местоимение</th>
          <th>Форма parler</th>
          <th>Перевод</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>je</td><td><strong>vais parler</strong></td><td>я собираюсь говорить</td></tr>
        <tr><td>tu</td><td><strong>vas parler</strong></td><td>ты собираешься говорить</td></tr>
        <tr><td>il / elle</td><td><strong>va parler</strong></td><td>он / она собирается говорить</td></tr>
        <tr><td>nous</td><td><strong>allons parler</strong></td><td>мы собираемся говорить</td></tr>
        <tr><td>vous</td><td><strong>allez parler</strong></td><td>вы собираетесь говорить</td></tr>
        <tr><td>ils / elles</td><td><strong>vont parler</strong></td><td>они собираются говорить</td></tr>
      </tbody>
    </table>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">💡</div>
      <div>
        <strong>Когда использовать futur proche:</strong><br>
        • Событие в ближайшем будущем: <em>Je vais sortir.</em><br>
        • Планы, которые точно сбудутся: <em>Nous allons voyager.</em><br>
        • Разговорная речь — очень часто.
      </div>
    </div>
  </div>

  <div class="lesson-section">
    <h3>📜 Шаг 2. Futur simple — простое будущее</h3>
    <p>
      Более формальное будущее. Схема: <strong>инфинитив + окончания</strong>.
      Окончания одинаковые для всех групп.
    </p>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Местоимение</th>
          <th>Окончание</th>
          <th>parler</th>
          <th>Перевод</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>je</td><td><strong>-ai</strong></td><td>je parler<strong>ai</strong></td><td>я поговорю</td></tr>
        <tr><td>tu</td><td><strong>-as</strong></td><td>tu parler<strong>as</strong></td><td>ты поговоришь</td></tr>
        <tr><td>il / elle</td><td><strong>-a</strong></td><td>il parler<strong>a</strong></td><td>он поговорит</td></tr>
        <tr><td>nous</td><td><strong>-ons</strong></td><td>nous parler<strong>ons</strong></td><td>мы поговорим</td></tr>
        <tr><td>vous</td><td><strong>-ez</strong></td><td>vous parler<strong>ez</strong></td><td>вы поговорите</td></tr>
        <tr><td>ils / elles</td><td><strong>-ont</strong></td><td>ils parler<strong>ont</strong></td><td>они поговорят</td></tr>
      </tbody>
    </table>

    <div class="lesson-callout lesson-callout-warn">
      <div class="callout-icon">⚠️</div>
      <div>
        <strong>У глаголов на -re</strong> конечная <em>-e</em> выпадает:
        <em>vendre</em> → <em>je vendrai</em> (не <s>vendreai</s>).
        У глаголов на -ir — прибавляем к инфинитиву напрямую:
        <em>finir</em> → <em>je finirai</em>.
      </div>
    </div>

    <p style="margin-top:18px;"><strong>Неправильные формы futur simple:</strong></p>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Глагол</th>
          <th>Основа будущего</th>
          <th>Пример</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>être</strong></td><td>ser-</td><td>je serai</td></tr>
        <tr><td><strong>avoir</strong></td><td>aur-</td><td>j'aurai</td></tr>
        <tr><td><strong>aller</strong></td><td>ir-</td><td>j'irai</td></tr>
        <tr><td><strong>faire</strong></td><td>fer-</td><td>je ferai</td></tr>
        <tr><td><strong>venir</strong></td><td>viendr-</td><td>je viendrai</td></tr>
        <tr><td><strong>voir</strong></td><td>verr-</td><td>je verrai</td></tr>
        <tr><td><strong>pouvoir</strong></td><td>pourr-</td><td>je pourrai</td></tr>
        <tr><td><strong>vouloir</strong></td><td>voudr-</td><td>je voudrai</td></tr>
        <tr><td><strong>savoir</strong></td><td>saur-</td><td>je saurai</td></tr>
        <tr><td><strong>devoir</strong></td><td>devr-</td><td>je devrai</td></tr>
      </tbody>
    </table>
  </div>

  <div class="lesson-section">
    <h3>🆚 Шаг 3. Futur proche vs Futur simple</h3>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Futur proche</th>
          <th>Futur simple</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Ближайшее, уже решённое</td>
          <td>Более далёкое, предположение</td>
        </tr>
        <tr>
          <td>Разговорный стиль</td>
          <td>Формальный, письменный</td>
        </tr>
        <tr>
          <td><em>Je vais partir demain.</em></td>
          <td><em>Je partirai un jour.</em></td>
        </tr>
        <tr>
          <td>Я уезжаю завтра.</td>
          <td>Я когда-нибудь уеду.</td>
        </tr>
      </tbody>
    </table>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">📌</div>
      <div>
        <strong>Маркеры будущего:</strong> demain (завтра),
        après-demain (послезавтра), la semaine prochaine (на следующей
        неделе), le mois prochain (в следующем месяце), bientôt (скоро),
        dans deux jours (через два дня).
      </div>
    </div>

    <div class="lesson-examples">
      <div class="example-row">
        <div class="example-fr">Je vais appeler ma mère.</div>
        <div class="example-ru">Я собираюсь позвонить маме.</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Nous irons à Paris l'année prochaine.</div>
        <div class="example-ru">Мы поедем в Париж в следующем году.</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Il fera beau demain.</div>
        <div class="example-ru">Завтра будет хорошая погода.</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Ils vont se marier bientôt.</div>
        <div class="example-ru">Они скоро поженятся.</div>
      </div>
    </div>

    <div class="lesson-mini-practice">
      <strong>🖊 Мини-практика:</strong>
      Поставь в futur proche, затем в futur simple:
      <br>1) Je (manger) une pizza. → <em>Je vais manger</em> / <em>Je mangerai</em>
      <br>2) Tu (aller) à Paris. → <em>Tu vas aller</em> / <em>Tu iras</em>
      <br>3) Nous (être) là. → <em>Nous allons être</em> / <em>Nous serons</em>
    </div>
  </div>

  <div class="lesson-section">
    <h3>📌 Что запомнить из урока 7</h3>
    <div class="lesson-cards">
      <div class="lesson-mini-card">
        <div class="mini-fr">vais parler</div>
        <div class="mini-pron">futur proche</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">parlerai</div>
        <div class="mini-pron">futur simple</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">ser-, aur-, ir-</div>
        <div class="mini-pron">неправильные основы</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">demain</div>
        <div class="mini-pron">маркер будущего</div>
      </div>
    </div>
  </div>

  <div class="lesson-task">
    <div class="task-head">
      <span class="task-badge">Практика</span>
      <h3>Закрепи материал</h3>
    </div>
    <ol>
      <li>Скажи в futur proche: «Я собираюсь поесть».</li>
      <li>Скажи в futur simple: «Мы поедем в Париж».</li>
      <li>Переведи: «Он позвонит завтра».</li>
      <li>Переведи: «Мы будем там в 5 часов».</li>
    </ol>
    <p class="task-hint">
      Подсказка: <em>Je vais manger · Nous irons à Paris ·
      Il appellera demain · Nous serons là à cinq heures</em>
    </p>
  </div>

  <div class="lesson-finish">
    <span class="finish-emoji">🎉</span>
    <strong>Félicitations !</strong>
    <p>Ты знаешь три времени: настоящее, прошедшее и будущее. Дальше — модальные глаголы.</p>
  </div>

</div>

<script>
(function () {
    var container = document.getElementById('quiz-container-7');
    if (!container) return;

    var QUESTIONS = [
        {
            prompt: 'Переведи на французский',
            ru: 'Я собираюсь поесть',
            words: ['Je', 'vais', 'manger', 'suis', 'le'],
            answer: ['Je', 'vais', 'manger']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'Мы поедем в Париж',
            words: ['Nous', 'irons', 'à', 'Paris', 'allons', 'le'],
            answer: ['Nous', 'irons', 'à', 'Paris']
        },
        {
            prompt: 'Переведи на русский',
            ru: 'Il fera beau demain',
            words: ['Завтра', 'будет', 'хорошая', 'погода', 'сегодня', 'идёт'],
            answer: ['Завтра', 'будет', 'хорошая', 'погода']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'Она позвонит завтра',
            words: ['Elle', 'appellera', 'demain', 'va', 'le'],
            answer: ['Elle', 'appellera', 'demain']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'Мы будем там в 5 часов',
            words: ['Nous', 'serons', 'là', 'à', 'cinq', 'heures', 'sommes'],
            answer: ['Nous', 'serons', 'là', 'à', 'cinq', 'heures']
        },
        {
            prompt: 'Переведи на русский',
            ru: 'Je vais partir',
            words: ['Я', 'собираюсь', 'уехать', 'поел', 'видел'],
            answer: ['Я', 'собираюсь', 'уехать']
        }
    ];

    var current = 0;
    var correctCount = 0;

    function render() {
        if (current >= QUESTIONS.length) {
            showFinish();
            return;
        }

        var q = QUESTIONS[current];
        var html = '';

        html += '<div class="quiz-question">';
        html += '<div class="quiz-progress">Вопрос ' + (current + 1) + ' из ' + QUESTIONS.length + '</div>';
        html += '<div class="quiz-prompt">' + q.prompt + '</div>';
        html += '<div class="quiz-ru">«' + q.ru + '»</div>';
        html += '<div class="quiz-answer" id="quiz-answer-7" data-placeholder="Нажимай на кирпичики ниже"></div>';

        var shuffled = q.words.slice().sort(function () { return Math.random() - 0.5; });

        html += '<div class="quiz-words" id="quiz-words-7">';
        shuffled.forEach(function (w) {
            html += '<button type="button" class="quiz-word" data-word="' + w + '">' + w + '</button>';
        });
        html += '</div>';

        html += '<div class="quiz-actions">';
        html += '<button type="button" class="btn btn-ghost" id="quiz-skip-7">Пропустить</button>';
        html += '<button type="button" class="btn btn-primary" id="quiz-check-7" disabled>Проверить</button>';
        html += '</div>';

        html += '<div class="quiz-feedback hidden" id="quiz-feedback-7"></div>';
        html += '</div>';

        container.innerHTML = html;
        bindEvents();
    }

    function bindEvents() {
        var answerZone = document.getElementById('quiz-answer-7');
        var wordsZone = document.getElementById('quiz-words-7');
        var checkBtn = document.getElementById('quiz-check-7');
        var skipBtn = document.getElementById('quiz-skip-7');
        var feedback = document.getElementById('quiz-feedback-7');
        var q = QUESTIONS[current];

        function updateCheck() {
            var picked = answerZone.querySelectorAll('.quiz-word').length;
            checkBtn.disabled = picked === 0;
        }

        wordsZone.addEventListener('click', function (e) {
            var btn = e.target.closest('.quiz-word');
            if (!btn || btn.disabled) return;
            var clone = document.createElement('button');
            clone.type = 'button';
            clone.className = 'quiz-word quiz-word-picked';
            clone.setAttribute('data-word', btn.getAttribute('data-word'));
            clone.textContent = btn.textContent;
            answerZone.appendChild(clone);
            btn.style.visibility = 'hidden';
            btn.disabled = true;
            updateCheck();
        });

        answerZone.addEventListener('click', function (e) {
            var btn = e.target.closest('.quiz-word');
            if (!btn) return;
            var word = btn.getAttribute('data-word');
            var source = Array.from(wordsZone.querySelectorAll('.quiz-word'))
                .find(function (b) {
                    return b.getAttribute('data-word') === word && b.disabled;
                });
            if (source) {
                source.style.visibility = 'visible';
                source.disabled = false;
            }
            btn.remove();
            updateCheck();
        });

        checkBtn.addEventListener('click', function () {
            var picked = Array.from(answerZone.querySelectorAll('.quiz-word'))
                .map(function (b) { return b.getAttribute('data-word'); });

            var isCorrect = picked.length === q.answer.length &&
                picked.every(function (w, i) { return w === q.answer[i]; });

            if (isCorrect) {
                correctCount++;
                showFeedback(true, 'Правильно! 🎉');
            } else {
                showFeedback(false, 'Не совсем. Правильно: ' + q.answer.join(' '));
            }

            checkBtn.disabled = true;
            skipBtn.disabled = true;

            setTimeout(function () {
                current++;
                render();
            }, 1500);
        });

        skipBtn.addEventListener('click', function () {
            showFeedback(false, 'Правильный ответ: ' + q.answer.join(' '));
            checkBtn.disabled = true;
            skipBtn.disabled = true;
            setTimeout(function () {
                current++;
                render();
            }, 1500);
        });

        function showFeedback(ok, text) {
            feedback.textContent = text;
            feedback.className = 'quiz-feedback ' + (ok ? 'quiz-feedback-ok' : 'quiz-feedback-no');
        }
    }

    function showFinish() {
        container.classList.add('hidden');
        var finish = document.getElementById('quiz-finish-7');
        finish.classList.remove('hidden');
        var score = document.getElementById('quiz-score-7');
        score.textContent = 'Правильных ответов: ' + correctCount + ' из ' + QUESTIONS.length;
    }

    render();
})();
</script>
"""


# =====================================================================
# УРОК 8 — МОДАЛЬНЫЕ ГЛАГОЛЫ
# =====================================================================

LESSON_8_HTML = """
<div class="lesson-block">

  <div class="lesson-intro">
    <span class="lesson-chip">🇫🇷 Français · Élémentaire · Урок 8</span>
    <h2>Модальные глаголы</h2>
    <p class="lesson-lead">
      Модальные глаголы показывают <strong>отношение говорящего</strong>:
      могу, должен, хочу, умею. Во французском их несколько, и они
      очень частотны. Освоив их, ты сможешь говорить о возможностях,
      желаниях и обязанностях.
    </p>
  </div>

  <div class="lesson-goals">
    <h3>🎯 Что ты узнаешь</h3>
    <ul>
      <li>Pouvoir — мочь</li>
      <li>Vouloir — хотеть</li>
      <li>Devoir — быть должным</li>
      <li>Savoir — знать, уметь</li>
      <li>Как строить фразы: «я хочу пойти», «я должен работать»</li>
    </ul>
  </div>

  <div class="lesson-section">
    <h3>💪 Шаг 1. Pouvoir — мочь</h3>
    <p>
      <strong>Pouvoir</strong> — «мочь, иметь возможность».
      Неправильный глагол. Спрягается так:
    </p>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Местоимение</th>
          <th>Форма</th>
          <th>Звучит как</th>
          <th>Перевод</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>je</td><td><strong>peux</strong></td><td><em>пё</em></td><td>я могу</td></tr>
        <tr><td>tu</td><td><strong>peux</strong></td><td><em>пё</em></td><td>ты можешь</td></tr>
        <tr><td>il / elle</td><td><strong>peut</strong></td><td><em>пё</em></td><td>он / она может</td></tr>
        <tr><td>nous</td><td><strong>pouvons</strong></td><td><em>пу-ВОН</em></td><td>мы можем</td></tr>
        <tr><td>vous</td><td><strong>pouvez</strong></td><td><em>пу-ВЭ</em></td><td>вы можете</td></tr>
        <tr><td>ils / elles</td><td><strong>peuvent</strong></td><td><em>пёв</em></td><td>они могут</td></tr>
      </tbody>
    </table>

    <div class="lesson-examples">
      <div class="example-row">
        <div class="example-fr">Je peux venir demain.</div>
        <div class="example-ru">Я могу прийти завтра.</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Est-ce que je peux entrer ?</div>
        <div class="example-ru">Можно войти?</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Nous ne pouvons pas attendre.</div>
        <div class="example-ru">Мы не можем ждать.</div>
      </div>
    </div>
  </div>

  <div class="lesson-section">
    <h3>💭 Шаг 2. Vouloir — хотеть</h3>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Местоимение</th>
          <th>Форма</th>
          <th>Звучит как</th>
          <th>Перевод</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>je</td><td><strong>veux</strong></td><td><em>вё</em></td><td>я хочу</td></tr>
        <tr><td>tu</td><td><strong>veux</strong></td><td><em>вё</em></td><td>ты хочешь</td></tr>
        <tr><td>il / elle</td><td><strong>veut</strong></td><td><em>вё</em></td><td>он / она хочет</td></tr>
        <tr><td>nous</td><td><strong>voulons</strong></td><td><em>ву-ЛОН</em></td><td>мы хотим</td></tr>
        <tr><td>vous</td><td><strong>voulez</strong></td><td><em>ву-ЛЭ</em></td><td>вы хотите</td></tr>
        <tr><td>ils / elles</td><td><strong>veulent</strong></td><td><em>вёль</em></td><td>они хотят</td></tr>
      </tbody>
    </table>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">💡</div>
      <div>
        <strong>Вежливая форма:</strong> <em>Je voudrais…</em> —
        «Я хотел бы…» (условное наклонение). Это вежливее, чем
        <em>Je veux</em>. Используй в кафе, магазине:
        <em>Je voudrais un café, s'il vous plaît.</em>
      </div>
    </div>

    <div class="lesson-examples">
      <div class="example-row">
        <div class="example-fr">Je veux apprendre le français.</div>
        <div class="example-ru">Я хочу учить французский.</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Elle veut partir.</div>
        <div class="example-ru">Она хочет уехать.</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Je voudrais un thé, s'il vous plaît.</div>
        <div class="example-ru">Я хотел бы чай, пожалуйста.</div>
      </div>
    </div>
  </div>

  <div class="lesson-section">
    <h3>⚠️ Шаг 3. Devoir — быть должным</h3>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Местоимение</th>
          <th>Форма</th>
          <th>Звучит как</th>
          <th>Перевод</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>je</td><td><strong>dois</strong></td><td><em>дуа</em></td><td>я должен</td></tr>
        <tr><td>tu</td><td><strong>dois</strong></td><td><em>дуа</em></td><td>ты должен</td></tr>
        <tr><td>il / elle</td><td><strong>doit</strong></td><td><em>дуа</em></td><td>он / она должен</td></tr>
        <tr><td>nous</td><td><strong>devons</strong></td><td><em>дё-ВОН</em></td><td>мы должны</td></tr>
        <tr><td>vous</td><td><strong>devez</strong></td><td><em>дё-ВЭ</em></td><td>вы должны</td></tr>
        <tr><td>ils / elles</td><td><strong>doivent</strong></td><td><em>дуав</em></td><td>они должны</td></tr>
      </tbody>
    </table>

    <div class="lesson-examples">
      <div class="example-row">
        <div class="example-fr">Je dois travailler.</div>
        <div class="example-ru">Я должен работать.</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Tu ne dois pas fumer.</div>
        <div class="example-ru">Ты не должен курить.</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Nous devons partir.</div>
        <div class="example-ru">Мы должны уйти.</div>
      </div>
    </div>
  </div>

  <div class="lesson-section">
    <h3>🧠 Шаг 4. Savoir — знать, уметь</h3>
    <p>
      <strong>Savoir</strong> означает «знать» (факт) или «уметь» (навык).
      Не путай с <em>connaître</em> — «быть знакомым».
    </p>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Местоимение</th>
          <th>Форма</th>
          <th>Звучит как</th>
          <th>Перевод</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>je</td><td><strong>sais</strong></td><td><em>сэ</em></td><td>я знаю / умею</td></tr>
        <tr><td>tu</td><td><strong>sais</strong></td><td><em>сэ</em></td><td>ты знаешь</td></tr>
        <tr><td>il / elle</td><td><strong>sait</strong></td><td><em>сэ</em></td><td>он / она знает</td></tr>
        <tr><td>nous</td><td><strong>savons</strong></td><td><em>са-ВОН</em></td><td>мы знаем</td></tr>
        <tr><td>vous</td><td><strong>savez</strong></td><td><em>са-ВЭ</em></td><td>вы знаете</td></tr>
        <tr><td>ils / elles</td><td><strong>savent</strong></td><td><em>сав</em></td><td>они знают</td></tr>
      </tbody>
    </table>

    <div class="lesson-callout lesson-callout-warn">
      <div class="callout-icon">⚠️</div>
      <div>
        <strong>Savoir vs Connaître:</strong><br>
        • <em>Je sais nager.</em> — Я умею плавать (навык).<br>
        • <em>Je connais Marie.</em> — Я знаю Мари (знаком).<br>
        • <em>Je sais la réponse.</em> — Я знаю ответ (факт).<br>
        • <em>Je connais Paris.</em> — Я знаю Париж (бывал там).
      </div>
    </div>
  </div>

  <div class="lesson-section">
    <h3>🔗 Шаг 5. Схема с модальными глаголами</h3>
    <p>
      После модального глагола — <strong>инфинитив без предлога</strong>.
      Это как в русском: «я хочу пойти» — два глагола подряд.
    </p>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">🧩</div>
      <div style="text-align:center; font-size: 1.05rem;">
        <strong>Модальный глагол + инфинитив</strong><br>
        <em>Je veux <strong>manger</strong></em> — Я хочу есть<br>
        <em>Je peux <strong>venir</strong></em> — Я могу прийти<br>
        <em>Je dois <strong>partir</strong></em> — Я должен уйти
      </div>
    </div>

    <p style="margin-top:18px;"><strong>Комбинации:</strong></p>

    <div class="lesson-examples">
      <div class="example-row">
        <div class="example-fr">Je veux pouvoir voyager.</div>
        <div class="example-ru">Я хочу иметь возможность путешествовать.</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Je dois savoir parler anglais.</div>
        <div class="example-ru">Я должен уметь говорить по-английски.</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Est-ce que tu peux m'aider ?</div>
        <div class="example-ru">Ты можешь мне помочь?</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Je ne veux pas partir.</div>
        <div class="example-ru">Я не хочу уходить.</div>
      </div>
    </div>

    <div class="lesson-mini-practice">
      <strong>🖊 Мини-практика:</strong>
      Переведи:
      <br>1) Я хочу пойти в кино → <em>Je veux aller au cinéma.</em>
      <br>2) Ты можешь помочь мне? → <em>Est-ce que tu peux m'aider ?</em>
      <br>3) Мы должны работать → <em>Nous devons travailler.</em>
      <br>4) Я умею плавать → <em>Je sais nager.</em>
    </div>
  </div>

  <div class="lesson-section">
    <h3>📌 Что запомнить из урока 8</h3>
    <div class="lesson-cards">
      <div class="lesson-mini-card">
        <div class="mini-fr">pouvoir</div>
        <div class="mini-pron">мочь</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">vouloir</div>
        <div class="mini-pron">хотеть</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">devoir</div>
        <div class="mini-pron">быть должным</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">savoir</div>
        <div class="mini-pron">знать / уметь</div>
      </div>
    </div>
  </div>

  <div class="lesson-task">
    <div class="task-head">
      <span class="task-badge">Практика</span>
      <h3>Закрепи материал</h3>
    </div>
    <ol>
      <li>Переведи: «Я хочу пойти в ресторан».</li>
      <li>Переведи: «Можно войти?»</li>
      <li>Переведи: «Ты должен учиться».</li>
      <li>Переведи: «Я умею говорить по-французски».</li>
    </ol>
    <p class="task-hint">
      Подсказка: <em>Je veux aller au restaurant ·
      Est-ce que je peux entrer ? ·
      Tu dois étudier · Je sais parler français</em>
    </p>
  </div>

  <div class="lesson-finish">
    <span class="finish-emoji">🎉</span>
    <strong>Félicitations !</strong>
    <p>Ты освоил модальные глаголы. Дальше — возвратные глаголы.</p>
  </div>

</div>

<script>
(function () {
    var container = document.getElementById('quiz-container-8');
    if (!container) return;

    var QUESTIONS = [
        {
            prompt: 'Переведи на французский',
            ru: 'Я хочу пойти в ресторан',
            words: ['Je', 'veux', 'aller', 'au', 'restaurant', 'peux'],
            answer: ['Je', 'veux', 'aller', 'au', 'restaurant']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'Можно войти?',
            words: ['Est-ce', 'que', 'je', 'peux', 'entrer', 'veux'],
            answer: ['Est-ce', 'que', 'je', 'peux', 'entrer']
        },
        {
            prompt: 'Переведи на русский',
            ru: 'Tu dois étudier',
            words: ['Ты', 'должен', 'учиться', 'хочешь', 'можешь'],
            answer: ['Ты', 'должен', 'учиться']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'Я умею плавать',
            words: ['Je', 'sais', 'nager', 'peux', 'veux', 'le'],
            answer: ['Je', 'sais', 'nager']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'Мы не можем ждать',
            words: ['Nous', 'ne', 'pouvons', 'pas', 'attendre', 'voulons'],
            answer: ['Nous', 'ne', 'pouvons', 'pas', 'attendre']
        },
        {
            prompt: 'Переведи на русский',
            ru: 'Je voudrais un café',
            words: ['Я', 'хотел', 'бы', 'кофе', 'должен', 'умею'],
            answer: ['Я', 'хотел', 'бы', 'кофе']
        }
    ];

    var current = 0;
    var correctCount = 0;

    function render() {
        if (current >= QUESTIONS.length) {
            showFinish();
            return;
        }

        var q = QUESTIONS[current];
        var html = '';

        html += '<div class="quiz-question">';
        html += '<div class="quiz-progress">Вопрос ' + (current + 1) + ' из ' + QUESTIONS.length + '</div>';
        html += '<div class="quiz-prompt">' + q.prompt + '</div>';
        html += '<div class="quiz-ru">«' + q.ru + '»</div>';
        html += '<div class="quiz-answer" id="quiz-answer-8" data-placeholder="Нажимай на кирпичики ниже"></div>';

        var shuffled = q.words.slice().sort(function () { return Math.random() - 0.5; });

        html += '<div class="quiz-words" id="quiz-words-8">';
        shuffled.forEach(function (w) {
            html += '<button type="button" class="quiz-word" data-word="' + w + '">' + w + '</button>';
        });
        html += '</div>';

        html += '<div class="quiz-actions">';
        html += '<button type="button" class="btn btn-ghost" id="quiz-skip-8">Пропустить</button>';
        html += '<button type="button" class="btn btn-primary" id="quiz-check-8" disabled>Проверить</button>';
        html += '</div>';

        html += '<div class="quiz-feedback hidden" id="quiz-feedback-8"></div>';
        html += '</div>';

        container.innerHTML = html;
        bindEvents();
    }

    function bindEvents() {
        var answerZone = document.getElementById('quiz-answer-8');
        var wordsZone = document.getElementById('quiz-words-8');
        var checkBtn = document.getElementById('quiz-check-8');
        var skipBtn = document.getElementById('quiz-skip-8');
        var feedback = document.getElementById('quiz-feedback-8');
        var q = QUESTIONS[current];

        function updateCheck() {
            var picked = answerZone.querySelectorAll('.quiz-word').length;
            checkBtn.disabled = picked === 0;
        }

        wordsZone.addEventListener('click', function (e) {
            var btn = e.target.closest('.quiz-word');
            if (!btn || btn.disabled) return;
            var clone = document.createElement('button');
            clone.type = 'button';
            clone.className = 'quiz-word quiz-word-picked';
            clone.setAttribute('data-word', btn.getAttribute('data-word'));
            clone.textContent = btn.textContent;
            answerZone.appendChild(clone);
            btn.style.visibility = 'hidden';
            btn.disabled = true;
            updateCheck();
        });

        answerZone.addEventListener('click', function (e) {
            var btn = e.target.closest('.quiz-word');
            if (!btn) return;
            var word = btn.getAttribute('data-word');
            var source = Array.from(wordsZone.querySelectorAll('.quiz-word'))
                .find(function (b) {
                    return b.getAttribute('data-word') === word && b.disabled;
                });
            if (source) {
                source.style.visibility = 'visible';
                source.disabled = false;
            }
            btn.remove();
            updateCheck();
        });

        checkBtn.addEventListener('click', function () {
            var picked = Array.from(answerZone.querySelectorAll('.quiz-word'))
                .map(function (b) { return b.getAttribute('data-word'); });

            var isCorrect = picked.length === q.answer.length &&
                picked.every(function (w, i) { return w === q.answer[i]; });

            if (isCorrect) {
                correctCount++;
                showFeedback(true, 'Правильно! 🎉');
            } else {
                showFeedback(false, 'Не совсем. Правильно: ' + q.answer.join(' '));
            }

            checkBtn.disabled = true;
            skipBtn.disabled = true;

            setTimeout(function () {
                current++;
                render();
            }, 1500);
        });

        skipBtn.addEventListener('click', function () {
            showFeedback(false, 'Правильный ответ: ' + q.answer.join(' '));
            checkBtn.disabled = true;
            skipBtn.disabled = true;
            setTimeout(function () {
                current++;
                render();
            }, 1500);
        });

        function showFeedback(ok, text) {
            feedback.textContent = text;
            feedback.className = 'quiz-feedback ' + (ok ? 'quiz-feedback-ok' : 'quiz-feedback-no');
        }
    }

    function showFinish() {
        container.classList.add('hidden');
        var finish = document.getElementById('quiz-finish-8');
        finish.classList.remove('hidden');
        var score = document.getElementById('quiz-score-8');
        score.textContent = 'Правильных ответов: ' + correctCount + ' из ' + QUESTIONS.length;
    }

    render();
})();
</script>
"""


# =====================================================================
# УРОК 9 — ВОЗВРАТНЫЕ ГЛАГОЛЫ
# =====================================================================

LESSON_9_HTML = """
<div class="lesson-block">

  <div class="lesson-intro">
    <span class="lesson-chip">🇫🇷 Français · Élémentaire · Урок 9</span>
    <h2>Возвратные глаголы</h2>
    <p class="lesson-lead">
      <strong>Возвратные глаголы</strong> — те, где действие направлено
      на себя: «я моюсь», «ты одеваешься», «мы встречаемся». Во французском
      их очень много, и они обозначаются частицей <em>se</em>.
      Ты узнаешь, как их спрягать и использовать в разных временах.
    </p>
  </div>

  <div class="lesson-goals">
    <h3>🎯 Что ты узнаешь</h3>
    <ul>
      <li>Что такое возвратные глаголы и зачем они нужны</li>
      <li>Частица <em>se</em> и её формы: me, te, se, nous, vous, se</li>
      <li>Спряжение в настоящем времени</li>
      <li>Отрицание и вопросы</li>
      <li>Прошедшее время с être</li>
    </ul>
  </div>

  <div class="lesson-section">
    <h3>🔄 Шаг 1. Что такое возвратный глагол</h3>
    <p>
      Возвратный глагол — это глагол, где <strong>подлежащее и дополнение
      совпадают</strong>. То есть «я делаю что-то с собой».
      В русском мы используем суффикс <em>-ся</em>: «моюсь», «одеваюсь».
      Во французском — частицу <em>se</em>.
    </p>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Обычный глагол</th>
          <th>Возвратный глагол</th>
          <th>Перевод</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>laver (мыть)</td>
          <td><strong>se laver</strong> (мыться)</td>
          <td>мыть себя</td>
        </tr>
        <tr>
          <td>habiller (одевать)</td>
          <td><strong>s'habiller</strong> (одеваться)</td>
          <td>одевать себя</td>
        </tr>
        <tr>
          <td>appeler (звать)</td>
          <td><strong>s'appeler</strong> (называться)</td>
          <td>звать себя</td>
        </tr>
        <tr>
          <td>lever (поднимать)</td>
          <td><strong>se lever</strong> (вставать)</td>
          <td>поднимать себя</td>
        </tr>
      </tbody>
    </table>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">💡</div>
      <div>
        <strong>Je m'appelle…</strong> — это как раз возвратный глагол!
        Ты уже его знаешь с урока 1. <em>Appeler</em> = «звать»,
        <em>s'appeler</em> = «звать себя» = «называться».
      </div>
    </div>
  </div>

  <div class="lesson-section">
    <h3>🔤 Шаг 2. Частица se и её формы</h3>
    <p>
      Частица <em>se</em> меняется в зависимости от подлежащего:
    </p>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Местоимение</th>
          <th>Частица</th>
          <th>Форма se laver</th>
          <th>Перевод</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>je</td><td><strong>me</strong> (m')</td><td>je <strong>me</strong> lave</td><td>я моюсь</td></tr>
        <tr><td>tu</td><td><strong>te</strong> (t')</td><td>tu <strong>te</strong> laves</td><td>ты моешься</td></tr>
        <tr><td>il / elle</td><td><strong>se</strong> (s')</td><td>il <strong>se</strong> lave</td><td>он моется</td></tr>
        <tr><td>nous</td><td><strong>nous</strong></td><td>nous <strong>nous</strong> lavons</td><td>мы моемся</td></tr>
        <tr><td>vous</td><td><strong>vous</strong></td><td>vous <strong>vous</strong> lavez</td><td>вы моетесь</td></tr>
        <tr><td>ils / elles</td><td><strong>se</strong> (s')</td><td>ils <strong>se</strong> lavent</td><td>они моются</td></tr>
      </tbody>
    </table>

    <div class="lesson-callout lesson-callout-warn">
      <div class="callout-icon">⚠️</div>
      <div>
        <strong>Элизия:</strong> перед гласной <em>me → m'</em>,
        <em>te → t'</em>, <em>se → s'</em>:<br>
        <em>Je <strong>m'</strong>appelle</em> — Я называюсь<br>
        <em>Tu <strong>t'</strong>habilles</em> — Ты одеваешься<br>
        <em>Il <strong>s'</strong>appelle</em> — Он называется
      </div>
    </div>
  </div>

  <div class="lesson-section">
    <h3>📚 Шаг 3. Частые возвратные глаголы</h3>

    <div class="lesson-cards">
      <div class="lesson-mini-card">
        <div class="mini-fr">se lever</div>
        <div class="mini-pron">сё лё-ВЭ</div>
        <div class="mini-ru">вставать</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">se coucher</div>
        <div class="mini-pron">сё ку-ШЕ</div>
        <div class="mini-ru">ложиться спать</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">s'habiller</div>
        <div class="mini-pron">са-би-ЙЕ</div>
        <div class="mini-ru">одеваться</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">se laver</div>
        <div class="mini-pron">сё ля-ВЭ</div>
        <div class="mini-ru">мыться</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">se réveiller</div>
        <div class="mini-pron">сё рэ-вэ-ЙЕ</div>
        <div class="mini-ru">просыпаться</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">s'amuser</div>
        <div class="mini-pron">са-мю-ЗЭ</div>
        <div class="mini-ru">развлекаться</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">se reposer</div>
        <div class="mini-pron">сё рё-по-ЗЭ</div>
        <div class="mini-ru">отдыхать</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">se dépêcher</div>
        <div class="mini-pron">сё дэ-пэ-ШЕ</div>
        <div class="mini-ru">торопиться</div>
      </div>
    </div>

    <div class="lesson-examples">
      <div class="example-row">
        <div class="example-fr">Je me lève à 7 heures.</div>
        <div class="example-ru">Я встаю в 7 часов.</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Elle s'habille rapidement.</div>
        <div class="example-ru">Она быстро одевается.</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Nous nous reposons le dimanche.</div>
        <div class="example-ru">Мы отдыхаем по воскресеньям.</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Ils s'amusent bien.</div>
        <div class="example-ru">Они хорошо развлекаются.</div>
      </div>
    </div>
  </div>

  <div class="lesson-section">
    <h3>🚫 Шаг 4. Отрицание и вопросы</h3>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">🧩</div>
      <div>
        <strong>Отрицание:</strong> ne + частица + глагол + pas<br>
        <em>Je <strong>ne me</strong> lave <strong>pas</strong>.</em> — Я не моюсь.<br>
        <em>Il <strong>ne s'</strong>habille <strong>pas</strong>.</em> — Он не одевается.<br><br>
        <strong>Вопрос:</strong> <em>Est-ce que tu te lèves tôt ?</em> —
        Ты рано встаёшь?
      </div>
    </div>
  </div>

  <div class="lesson-section">
    <h3>📅 Шаг 5. Прошедшее время</h3>
    <p>
      Возвратные глаголы в passé composé всегда спрягаются
      с <strong>être</strong>, и причастие согласуется с подлежащим.
    </p>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Местоимение</th>
          <th>Passé composé</th>
          <th>Перевод</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>je</td><td>je me suis levé(e)</td><td>я встал(а)</td></tr>
        <tr><td>tu</td><td>tu t'es levé(e)</td><td>ты встал(а)</td></tr>
        <tr><td>il</td><td>il s'est levé</td><td>он встал</td></tr>
        <tr><td>elle</td><td>elle s'est levée</td><td>она встала</td></tr>
        <tr><td>nous</td><td>nous nous sommes levé(e)s</td><td>мы встали</td></tr>
        <tr><td>vous</td><td>vous vous êtes levé(e)(s)</td><td>вы встали</td></tr>
        <tr><td>ils</td><td>ils se sont levés</td><td>они встали (м.)</td></tr>
        <tr><td>elles</td><td>elles se sont levées</td><td>они встали (ж.)</td></tr>
      </tbody>
    </table>

    <div class="lesson-callout lesson-callout-warn">
      <div class="callout-icon">⚠️</div>
      <div>
        <strong>Отрицание в passé composé:</strong> <em>ne</em> ставится
        перед частицей, <em>pas</em> — после вспомогательного глагола:<br>
        <em>Je <strong>ne me suis pas</strong> levé.</em> — Я не встал.
      </div>
    </div>

    <div class="lesson-mini-practice">
      <strong>🖊 Мини-практика:</strong>
      Переведи:
      <br>1) Я встаю в 6 утра → <em>Je me lève à six heures.</em>
      <br>2) Она не торопится → <em>Elle ne se dépêche pas.</em>
      <br>3) Мы отдохнули вчера → <em>Nous nous sommes reposés hier.</em>
    </div>
  </div>

  <div class="lesson-section">
    <h3>📌 Что запомнить из урока 9</h3>
    <div class="lesson-cards">
      <div class="lesson-mini-card">
        <div class="mini-fr">se laver</div>
        <div class="mini-pron">мыться</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">me, te, se…</div>
        <div class="mini-pron">частицы</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">je me lève</div>
        <div class="mini-pron">настоящее</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">je me suis levé</div>
        <div class="mini-pron">прошедшее с être</div>
      </div>
    </div>
  </div>

  <div class="lesson-task">
    <div class="task-head">
      <span class="task-badge">Практика</span>
      <h3>Закрепи материал</h3>
    </div>
    <ol>
      <li>Переведи: «Я встаю в 7 утра».</li>
      <li>Переведи: «Она быстро одевается».</li>
      <li>Переведи: «Мы не отдыхаем сегодня».</li>
      <li>Переведи: «Они встали поздно» (passé composé).</li>
    </ol>
    <p class="task-hint">
      Подсказка: <em>Je me lève à sept heures ·
      Elle s'habille rapidement ·
      Nous ne nous reposons pas aujourd'hui ·
      Ils se sont levés tard</em>
    </p>
  </div>

  <div class="lesson-finish">
    <span class="finish-emoji">🎉</span>
    <strong>Félicitations !</strong>
    <p>Ты освоил возвратные глаголы. Дальше — финальный урок с итоговой контрольной.</p>
  </div>

</div>

<script>
(function () {
    var container = document.getElementById('quiz-container-9');
    if (!container) return;

    var QUESTIONS = [
        {
            prompt: 'Переведи на французский',
            ru: 'Я встаю в 7 утра',
            words: ['Je', 'me', 'lève', 'à', 'sept', 'heures', 'suis'],
            answer: ['Je', 'me', 'lève', 'à', 'sept', 'heures']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'Она быстро одевается',
            words: ['Elle', 's\\'', 'habille', 'rapidement', 'se', 'est'],
            answer: ['Elle', 's\\'', 'habille', 'rapidement']
        },
        {
            prompt: 'Переведи на русский',
            ru: 'Nous nous reposons',
            words: ['Мы', 'отдыхаем', 'моемся', 'одеваемся', 'идём'],
            answer: ['Мы', 'отдыхаем']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'Я не моюсь',
            words: ['Je', 'ne', 'me', 'lave', 'pas', 'suis'],
            answer: ['Je', 'ne', 'me', 'lave', 'pas']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'Они встали поздно',
            words: ['Ils', 'se', 'sont', 'levés', 'tard', 'ont'],
            answer: ['Ils', 'se', 'sont', 'levés', 'tard']
        },
        {
            prompt: 'Переведи на русский',
            ru: 'Elle ne se dépêche pas',
            words: ['Она', 'не', 'торопится', 'моется', 'одевается'],
            answer: ['Она', 'не', 'торопится']
        }
    ];

    var current = 0;
    var correctCount = 0;

    function render() {
        if (current >= QUESTIONS.length) {
            showFinish();
            return;
        }

        var q = QUESTIONS[current];
        var html = '';

        html += '<div class="quiz-question">';
        html += '<div class="quiz-progress">Вопрос ' + (current + 1) + ' из ' + QUESTIONS.length + '</div>';
        html += '<div class="quiz-prompt">' + q.prompt + '</div>';
        html += '<div class="quiz-ru">«' + q.ru + '»</div>';
        html += '<div class="quiz-answer" id="quiz-answer-9" data-placeholder="Нажимай на кирпичики ниже"></div>';

        var shuffled = q.words.slice().sort(function () { return Math.random() - 0.5; });

        html += '<div class="quiz-words" id="quiz-words-9">';
        shuffled.forEach(function (w) {
            html += '<button type="button" class="quiz-word" data-word="' + w + '">' + w + '</button>';
        });
        html += '</div>';

        html += '<div class="quiz-actions">';
        html += '<button type="button" class="btn btn-ghost" id="quiz-skip-9">Пропустить</button>';
        html += '<button type="button" class="btn btn-primary" id="quiz-check-9" disabled>Проверить</button>';
        html += '</div>';

        html += '<div class="quiz-feedback hidden" id="quiz-feedback-9"></div>';
        html += '</div>';

        container.innerHTML = html;
        bindEvents();
    }

    function bindEvents() {
        var answerZone = document.getElementById('quiz-answer-9');
        var wordsZone = document.getElementById('quiz-words-9');
        var checkBtn = document.getElementById('quiz-check-9');
        var skipBtn = document.getElementById('quiz-skip-9');
        var feedback = document.getElementById('quiz-feedback-9');
        var q = QUESTIONS[current];

        function updateCheck() {
            var picked = answerZone.querySelectorAll('.quiz-word').length;
            checkBtn.disabled = picked === 0;
        }

        wordsZone.addEventListener('click', function (e) {
            var btn = e.target.closest('.quiz-word');
            if (!btn || btn.disabled) return;
            var clone = document.createElement('button');
            clone.type = 'button';
            clone.className = 'quiz-word quiz-word-picked';
            clone.setAttribute('data-word', btn.getAttribute('data-word'));
            clone.textContent = btn.textContent;
            answerZone.appendChild(clone);
            btn.style.visibility = 'hidden';
            btn.disabled = true;
            updateCheck();
        });

        answerZone.addEventListener('click', function (e) {
            var btn = e.target.closest('.quiz-word');
            if (!btn) return;
            var word = btn.getAttribute('data-word');
            var source = Array.from(wordsZone.querySelectorAll('.quiz-word'))
                .find(function (b) {
                    return b.getAttribute('data-word') === word && b.disabled;
                });
            if (source) {
                source.style.visibility = 'visible';
                source.disabled = false;
            }
            btn.remove();
            updateCheck();
        });

        checkBtn.addEventListener('click', function () {
            var picked = Array.from(answerZone.querySelectorAll('.quiz-word'))
                .map(function (b) { return b.getAttribute('data-word'); });

            var isCorrect = picked.length === q.answer.length &&
                picked.every(function (w, i) { return w === q.answer[i]; });

            if (isCorrect) {
                correctCount++;
                showFeedback(true, 'Правильно! 🎉');
            } else {
                showFeedback(false, 'Не совсем. Правильно: ' + q.answer.join(' '));
            }

            checkBtn.disabled = true;
            skipBtn.disabled = true;

            setTimeout(function () {
                current++;
                render();
            }, 1500);
        });

        skipBtn.addEventListener('click', function () {
            showFeedback(false, 'Правильный ответ: ' + q.answer.join(' '));
            checkBtn.disabled = true;
            skipBtn.disabled = true;
            setTimeout(function () {
                current++;
                render();
            }, 1500);
        });

        function showFeedback(ok, text) {
            feedback.textContent = text;
            feedback.className = 'quiz-feedback ' + (ok ? 'quiz-feedback-ok' : 'quiz-feedback-no');
        }
    }

    function showFinish() {
        container.classList.add('hidden');
        var finish = document.getElementById('quiz-finish-9');
        finish.classList.remove('hidden');
        var score = document.getElementById('quiz-score-9');
        score.textContent = 'Правильных ответов: ' + correctCount + ' из ' + QUESTIONS.length;
    }

    render();
})();
</script>
"""


# =====================================================================
# УРОК 10 — ФИНАЛЬНЫЙ УРОК И ИТОГОВАЯ КОНТРОЛЬНАЯ
# =====================================================================

LESSON_10_HTML = """
<div class="lesson-block">

  <div class="lesson-intro">
    <span class="lesson-chip">🇫🇷 Français · Élémentaire · Урок 10</span>
    <h2>Практика и итоговая контрольная</h2>
    <p class="lesson-lead">
      Финальный урок. Мы соберём всё, что ты узнал за курс: местоимения,
      времена, вопросы, модальные и возвратные глаголы. Ты научишься
      строить <strong>связный рассказ о себе</strong>, и в конце
      пройдёшь <strong>итоговую контрольную</strong>.
    </p>
  </div>

  <div class="lesson-goals">
    <h3>🎯 Что ты узнаешь</h3>
    <ul>
      <li>Как рассказать о себе по-французски</li>
      <li>Связки: et, mais, parce que, donc</li>
      <li>Полезные разговорные фразы</li>
      <li>Типичные ошибки русскоговорящих</li>
      <li>Пройдёшь итоговую контрольную по всему курсу</li>
    </ul>
  </div>

  <div class="lesson-section">
    <h3>👤 Шаг 1. Рассказ о себе</h3>
    <p>
      Рассказ о себе строится по простой схеме. Вот пример:
    </p>

    <div class="lesson-callout lesson-callout-info">
      <div class="callout-icon">📝</div>
      <div>
        <strong>Je m'appelle Anna. J'ai 25 ans. Je suis russe.
        J'habite à Moscou. Je suis designer. Je travaille dans
        une petite entreprise. J'aime lire et jouer au tennis.
        Je sais parler anglais et français. Je veux voyager
        aux États-Unis. Hier, je suis allée au cinéma avec
        mes amis. Demain, je vais travailler.</strong>
      </div>
    </div>

    <p style="margin-top:18px;"><strong>Схема рассказа:</strong></p>
    <ul>
      <li>Имя: <em>Je m'appelle…</em></li>
      <li>Возраст: <em>J'ai … ans.</em></li>
      <li>Национальность: <em>Je suis russe.</em></li>
      <li>Где живёшь: <em>J'habite à…</em></li>
      <li>Профессия: <em>Je suis … / Je travaille…</em></li>
      <li>Увлечения: <em>J'aime + инфинитив</em></li>
      <li>Умения: <em>Je sais…</em></li>
      <li>Планы: <em>Je veux…</em></li>
      <li>Прошлое: <em>Hier, je suis allé(e)…</em></li>
      <li>Будущее: <em>Demain, je vais…</em></li>
    </ul>
  </div>

  <div class="lesson-section">
    <h3>🔗 Шаг 2. Связки</h3>
    <p>
      Чтобы речь звучала естественно, используй связки.
    </p>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Français</th>
          <th>Звучит как</th>
          <th>Перевод</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>et</strong></td><td><em>э</em></td><td>и</td></tr>
        <tr><td><strong>mais</strong></td><td><em>мэ</em></td><td>но</td></tr>
        <tr><td><strong>ou</strong></td><td><em>у</em></td><td>или</td></tr>
        <tr><td><strong>parce que</strong></td><td><em>парс-КЁ</em></td><td>потому что</td></tr>
        <tr><td><strong>donc</strong></td><td><em>донк</em></td><td>поэтому</td></tr>
        <tr><td><strong>aussi</strong></td><td><em>о-СИ</em></td><td>также</td></tr>
        <tr><td><strong>alors</strong></td><td><em>а-ЛОР</em></td><td>тогда / итак</td></tr>
      </tbody>
    </table>

    <div class="lesson-examples">
      <div class="example-row">
        <div class="example-fr">J'aime le thé et le café.</div>
        <div class="example-ru">Я люблю чай и кофе.</div>
      </div>
      <div class="example-row">
        <div class="example-fr">Je suis fatigué mais heureux.</div>
        <div class="example-ru">Я устал, но счастлив.</div>
      </div>
      <div class="example-row">
        <div class="example-fr">J'apprends le français parce que je veux voyager.</div>
        <div class="example-ru">Я учу французский, потому что хочу путешествовать.</div>
      </div>
    </div>
  </div>

  <div class="lesson-section">
    <h3>💬 Шаг 3. Полезные разговорные фразы</h3>

    <div class="lesson-cards">
      <div class="lesson-mini-card">
        <div class="mini-fr">Comment ça va ?</div>
        <div class="mini-pron">ко-МАН са ВА</div>
        <div class="mini-ru">Как дела?</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">Ça va bien</div>
        <div class="mini-pron">са ва БЬЕН</div>
        <div class="mini-ru">Всё хорошо</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">Excusez-moi</div>
        <div class="mini-pron">экс-кю-ЗЭ-муа</div>
        <div class="mini-ru">Извините</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">Pardon</div>
        <div class="mini-pron">пар-ДОН</div>
        <div class="mini-ru">Простите</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">Merci</div>
        <div class="mini-pron">мер-СИ</div>
        <div class="mini-ru">Спасибо</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">De rien</div>
        <div class="mini-pron">дё РЬЕН</div>
        <div class="mini-ru">Не за что</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">S'il vous plaît</div>
        <div class="mini-pron">силь ву ПЛЭ</div>
        <div class="mini-ru">Пожалуйста (вежл.)</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">Je ne comprends pas</div>
        <div class="mini-pron">жё нё ком-ПРАН па</div>
        <div class="mini-ru">Я не понимаю</div>
      </div>
    </div>
  </div>

  <div class="lesson-section">
    <h3>⚠️ Шаг 4. Типичные ошибки</h3>

    <table class="lesson-table">
      <thead>
        <tr>
          <th>Ошибка</th>
          <th>Правильно</th>
          <th>Почему</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><s>Je suis 25 ans</s></td>
          <td>J'ai 25 ans</td>
          <td>Возраст через avoir</td>
        </tr>
        <tr>
          <td><s>Je suis d'accord</s></td>
          <td>Je suis d'accord</td>
          <td>Здесь être — правильно</td>
        </tr>
        <tr>
          <td><s>Je aime</s></td>
          <td>J'aime</td>
          <td>Элизия обязательна</td>
        </tr>
        <tr>
          <td><s>Elle est allé</s></td>
          <td>Elle est allée</td>
          <td>С être — согласование</td>
        </tr>
        <tr>
          <td><s>Je veux de manger</s></td>
          <td>Je veux manger</td>
          <td>После модального — без предлога</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- === ИТОГОВАЯ КОНТРОЛЬНАЯ === -->
  <div class="lesson-quiz">
    <div class="quiz-head">
      <span class="quiz-badge">Итоговая контрольная</span>
      <h3>Проверь себя</h3>
      <p class="text-muted">Собери правильные ответы. Клик по выбранному слову — вернуть обратно.</p>
    </div>

    <div id="quiz-container-10"></div>

    <div class="quiz-finish hidden" id="quiz-finish-10">
      <span class="finish-emoji">🏆</span>
      <strong>Курс пройден!</strong>
      <p id="quiz-score-10"></p>
    </div>
  </div>

  <div class="lesson-section" style="margin-top:32px;">
    <h3>📌 Что запомнить из урока 10</h3>
    <div class="lesson-cards">
      <div class="lesson-mini-card">
        <div class="mini-fr">Je m'appelle…</div>
        <div class="mini-pron">рассказ о себе</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">et, mais, parce que</div>
        <div class="mini-pron">связки</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">Comment ça va ?</div>
        <div class="mini-pron">разговорные фразы</div>
      </div>
      <div class="lesson-mini-card">
        <div class="mini-fr">J'ai 25 ans</div>
        <div class="mini-pron">возраст через avoir</div>
      </div>
    </div>
  </div>

  <div class="lesson-finish">
    <span class="finish-emoji">🏆</span>
    <strong>Félicitations !</strong>
    <p>Ты прошёл весь курс французского. Теперь ты можешь говорить о себе, о прошлом, настоящем и будущем, задавать вопросы, использовать модальные и возвратные глаголы. Дальше — практика с носителями и расширение словарного запаса.</p>
  </div>

</div>

<script>
(function () {
    var container = document.getElementById('quiz-container-10');
    if (!container) return;

    var QUESTIONS = [
        {
            prompt: 'Переведи на французский',
            ru: 'Меня зовут Анна',
            words: ['Je', 'm\\'', 'appelle', 'Anna', 'suis', 'le'],
            answer: ['Je', 'm\\'', 'appelle', 'Anna']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'Мне 25 лет',
            words: ['J\\'', 'ai', '25', 'ans', 'suis', 'un'],
            answer: ['J\\'', 'ai', '25', 'ans']
        },
        {
            prompt: 'Переведи на русский',
            ru: 'Je suis allé au cinéma',
            words: ['Я', 'пошёл', 'в', 'кино', 'собираюсь', 'видел'],
            answer: ['Я', 'пошёл', 'в', 'кино']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'Я хочу учить французский',
            words: ['Je', 'veux', 'apprendre', 'le', 'français', 'peux'],
            answer: ['Je', 'veux', 'apprendre', 'le', 'français']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'Я встаю в 7 утра',
            words: ['Je', 'me', 'lève', 'à', 'sept', 'heures', 'suis'],
            answer: ['Je', 'me', 'lève', 'à', 'sept', 'heures']
        },
        {
            prompt: 'Переведи на русский',
            ru: 'Nous irons à Paris',
            words: ['Мы', 'поедем', 'в', 'Париж', 'поехали', 'идём'],
            answer: ['Мы', 'поедем', 'в', 'Париж']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'Она не говорит по-французски',
            words: ['Elle', 'ne', 'parle', 'pas', 'français', 'est'],
            answer: ['Elle', 'ne', 'parle', 'pas', 'français']
        },
        {
            prompt: 'Переведи на французский',
            ru: 'Я никогда не курю',
            words: ['Je', 'ne', 'fume', 'jamais', 'pas', 'suis'],
            answer: ['Je', 'ne', 'fume', 'jamais']
        }
    ];

    var current = 0;
    var correctCount = 0;

    function render() {
        if (current >= QUESTIONS.length) {
            showFinish();
            return;
        }

        var q = QUESTIONS[current];
        var html = '';

        html += '<div class="quiz-question">';
        html += '<div class="quiz-progress">Вопрос ' + (current + 1) + ' из ' + QUESTIONS.length + '</div>';
        html += '<div class="quiz-prompt">' + q.prompt + '</div>';
        html += '<div class="quiz-ru">«' + q.ru + '»</div>';
        html += '<div class="quiz-answer" id="quiz-answer-10" data-placeholder="Нажимай на кирпичики ниже"></div>';

        var shuffled = q.words.slice().sort(function () { return Math.random() - 0.5; });

        html += '<div class="quiz-words" id="quiz-words-10">';
        shuffled.forEach(function (w) {
            html += '<button type="button" class="quiz-word" data-word="' + w + '">' + w + '</button>';
        });
        html += '</div>';

        html += '<div class="quiz-actions">';
        html += '<button type="button" class="btn btn-ghost" id="quiz-skip-10">Пропустить</button>';
        html += '<button type="button" class="btn btn-primary" id="quiz-check-10" disabled>Проверить</button>';
        html += '</div>';

        html += '<div class="quiz-feedback hidden" id="quiz-feedback-10"></div>';
        html += '</div>';

        container.innerHTML = html;
        bindEvents();
    }

    function bindEvents() {
        var answerZone = document.getElementById('quiz-answer-10');
        var wordsZone = document.getElementById('quiz-words-10');
        var checkBtn = document.getElementById('quiz-check-10');
        var skipBtn = document.getElementById('quiz-skip-10');
        var feedback = document.getElementById('quiz-feedback-10');
        var q = QUESTIONS[current];

        function updateCheck() {
            var picked = answerZone.querySelectorAll('.quiz-word').length;
            checkBtn.disabled = picked === 0;
        }

        wordsZone.addEventListener('click', function (e) {
            var btn = e.target.closest('.quiz-word');
            if (!btn || btn.disabled) return;
            var clone = document.createElement('button');
            clone.type = 'button';
            clone.className = 'quiz-word quiz-word-picked';
            clone.setAttribute('data-word', btn.getAttribute('data-word'));
            clone.textContent = btn.textContent;
            answerZone.appendChild(clone);
            btn.style.visibility = 'hidden';
            btn.disabled = true;
            updateCheck();
        });

        answerZone.addEventListener('click', function (e) {
            var btn = e.target.closest('.quiz-word');
            if (!btn) return;
            var word = btn.getAttribute('data-word');
            var source = Array.from(wordsZone.querySelectorAll('.quiz-word'))
                .find(function (b) {
                    return b.getAttribute('data-word') === word && b.disabled;
                });
            if (source) {
                source.style.visibility = 'visible';
                source.disabled = false;
            }
            btn.remove();
            updateCheck();
        });

        checkBtn.addEventListener('click', function () {
            var picked = Array.from(answerZone.querySelectorAll('.quiz-word'))
                .map(function (b) { return b.getAttribute('data-word'); });

            var isCorrect = picked.length === q.answer.length &&
                picked.every(function (w, i) { return w === q.answer[i]; });

            if (isCorrect) {
                correctCount++;
                showFeedback(true, 'Правильно! 🎉');
            } else {
                showFeedback(false, 'Не совсем. Правильно: ' + q.answer.join(' '));
            }

            checkBtn.disabled = true;
            skipBtn.disabled = true;

            setTimeout(function () {
                current++;
                render();
            }, 1500);
        });

        skipBtn.addEventListener('click', function () {
            showFeedback(false, 'Правильный ответ: ' + q.answer.join(' '));
            checkBtn.disabled = true;
            skipBtn.disabled = true;
            setTimeout(function () {
                current++;
                render();
            }, 1500);
        });

        function showFeedback(ok, text) {
            feedback.textContent = text;
            feedback.className = 'quiz-feedback ' + (ok ? 'quiz-feedback-ok' : 'quiz-feedback-no');
        }
    }

    function showFinish() {
        container.classList.add('hidden');
        var finish = document.getElementById('quiz-finish-10');
        finish.classList.remove('hidden');
        var score = document.getElementById('quiz-score-10');
        score.textContent = 'Правильных ответов: ' + correctCount + ' из ' + QUESTIONS.length;
    }

    render();
})();
</script>
"""


