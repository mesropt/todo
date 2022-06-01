import React from 'react'

const ToDoItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.project}</td>
            <td>{item.note_text}</td>
            <td>{item.date_created}</td>
            <td>{item.date_updated}</td>
            <td>{item.author}</td>
            <td>{item.execution_status}</td>
        </tr>
    )
}

const ToDoList = ({items}) => {
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>Project name</th>
                <th>Note text</th>
                <th>Date created</th>
                <th>Date updated</th>
                <th>Author</th>
                <th>Execution status</th>
            </tr>
            {items.map((item) => <ToDoItem item={item} />)}
        </table>
    )
}

export default ToDoList;