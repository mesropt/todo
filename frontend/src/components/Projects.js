import React from 'react'
import ToDoList from "./ToDos";

const ProjectItem = ({item}) => {
    return (
        <tr>
            <td>{item.projectName}</td>
            <td>{item.repositoryLink}</td>
            <td>{item.users}</td>
        </tr>
    )
}

const ProjectList = ({items}) => {
    return (
        <table>
            <tr>
                <th>Project Name</th>
                <th>Repository Link</th>
                <th>Participating Users</th>
            </tr>
            {items.map((item) => <ProjectItem item={item} />)}
        </table>
    )
}


export default ProjectList;