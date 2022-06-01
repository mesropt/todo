import React from 'react'

const UserItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.username}</td>
            <td>{item.firstname}</td>
            <td>{item.lastname}</td>
            <td>{item.email}</td>
        </tr>
    )
}

const UserList = ({items}) => {
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>Username</th>
                <th>Firstname</th>
                <th>Lastname</th>
                <th>Email</th>
            </tr>
            {items.map((item) => <UserItem item={item} />)}
        </table>
    )
}

export default UserList;