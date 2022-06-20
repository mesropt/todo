import React from 'react'
import {Link} from "react-router-dom";


const ToDoItem = ({item, deleteToDo}) => {
    return (
        <tr>
            <td>{item.project}</td>
            <td>{item.noteText}</td>
            <td>{item.dateCreated}</td>
            <td>{item.dateUpdated}</td>
            <td>{item.author}</td>
            <td>{item.executionStatus}</td>
            <td><button onClick={() => deleteToDo(item.url)} type="button">Delete</button></td>
        </tr>
    )
}


const ToDoList = ({items, deleteTodo}) => {
    return (
        <div className={"container"}>
            <table className={"table table-bordered table-hover"}>
                <thead className={"table-light"}>
                <tr>
                    <th scope={"col"}>Project</th>
                    <th scope={"col"}>Note text</th>
                    <th scope={"col"}>Date created</th>
                    <th scope={"col"}>Date updated</th>
                    <th scope={"col"}>Author</th>
                    <th scope={"col"}>Execution status</th>
                </tr>
                </thead>
                <tbody>
                {items.map((item, index) => <ToDoItem item={item} deleteToDo={deleteTodo} key={index}/>)}
                </tbody>
            </table>
            <Link to='/todos/create' className='btn btn-primary'>Create</Link>
        </div>
    )
}

export default ToDoList;