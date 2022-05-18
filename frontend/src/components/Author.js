import React from 'react';

const AuthorItem = ({author}) => { // Это простой компонент без состояния. Такие компоненты удобно создавать как функции. В параметры каждого компонента на React приходит объект props, который мы создавали в App.js. props - это объект, который содержит в себе все переданные компоненты данные. И здесь параметр ({author}) означает, что из всех props мы ожидаем получить author - объект автора, и дальше работать только с ним. Далее ниже возвращается html код. Данная функция отрабатывается на компьютере пользователя, всё это рендеря.
    return (
        <tr>
            <td>
                {author.first_name}
            </td>
            <td>
                {author.last_name}
            </td>
            <td>
                {author.birthday_year}
            </td>
        </tr>
    )
}

const AuthorList = ({authors}) => { // Это компонент для списка авторов.
    return (
        <table>
            <th>
                First Name
            </th>
            <th>
                Last Name
            </th>
            <th>
                Birthday year
            </th>
            {authors.map((author) => <AuthorItem author={author} />)}
        </table> // Комментарий к вышестоящей строке: authors - это массив данных об авторе. map превращает каждого автора из массива в соответствующий компонент AuthorItem.
    )
}

export default AuthorList;