import React from 'react'

const ProjectItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.project_name}</td>
            <td>{item.repository_link}</td>
            <td>{item.users}</td>
        </tr>
    )
}

const ProjectList = ({items}) => {
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>Project name</th>
                <th>Repository link</th>
                <th>Involved users</th>
            </tr>
            {items.map((item) => <ProjectItem item={item} />)}
        </table>
    )
}

export default ProjectList;