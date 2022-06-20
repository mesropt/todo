import React from 'react'
import {Link} from "react-router-dom";


const UserItem = ({item, deleteUser}) => {
    return (
        <tr>
            <td>{item.username}</td>
            <td>{item.firstname}</td>
            <td>{item.lastname}</td>
            <td>{item.email}</td>
            <td><button onClick={() => deleteUser(item.id)} type="button">Delete</button></td>
        </tr>
    )
}

const UserList = ({items, deleteUser}) => {
    return (
        <div className={"container"}>
            <table className={"table table-bordered table-hover"}>
                <thead className={"table-light"}>
                <tr>
                    <th scope={"col"}>Username</th>
                    <th scope={"col"}>First name</th>
                    <th scope={"col"}>Last name</th>
                    <th scope={"col"}>Email</th>
                    <th></th>
                </tr>
                </thead>
                <tbody>
                {items.map((item, index) => <UserItem item={item} deleteUser={deleteUser} key={index}/>)}
                </tbody>
            </table>
            <Link to='users/create'>Create</Link>
        </div>
    )
}
// ----------------------------------------------------------------------------
export default UserList;