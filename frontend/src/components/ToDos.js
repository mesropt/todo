import React from 'react'


const TodoItem = ({item}) => {
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


const TodoList = ({items}) => {
    return (
        <div className={"container"}>
            <table className={"table table-bordered table-hover"}>
                <thead className={"table-light"}>
                <tr>
                    <th scope={"col"}>ID</th>
                    <th scope={"col"}>Project</th>
                    <th scope={"col"}>Note text</th>
                    <th scope={"col"}>Date created</th>
                    <th scope={"col"}>Date updated</th>
                    <th scope={"col"}>Author</th>
                    <th scope={"col"}>Execution status</th>
                </tr>
                </thead>
                <tbody>
                {items.map((item, index) => <TodoItem item={item} key={index}/>)}
                </tbody>
            </table>
        </div>
    )
}

export default TodoList;