import React from 'react';

const UserItem = ({user}) => { // Это простой компонент без состояния. Такие компоненты удобно создавать как функции. В параметры каждого компонента на React приходит объект props, который мы создавали в App.js. props - это объект, который содержит в себе все переданные компоненты данные. И здесь параметр ({author}) означает, что из всех props мы ожидаем получить author - объект автора, и дальше работать только с ним. Далее ниже возвращается html код. Данная функция отрабатывается на компьютере пользователя, всё это рендеря.
    return (
        <tr>
            <td>
                {user.username}
            </td>
            <td>
                {user.firstname}
            </td>
            <td>
                {user.lastname}
            </td>
            <td>
                {user.email}
            </td>
        </tr>
    )
}

const UserList = ({users}) => { // Это компонент для списка авторов.
    return (
        <table>
            <th>
                Username
            </th>
            <th>
                Firstname
            </th>
            <th>
                Lastname
            </th>
            <th>
                Email
            </th>
            {users.map((user) => <UserItem user={user} />)}
        </table> // Комментарий к вышестоящей строке: users - это массив данных об авторе. map превращает каждого автора из массива в соответствующий компонент AuthorItem.
    )
}

export default UserList;