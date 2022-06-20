import React from 'react'
import {Link} from "react-router-dom";

const ProjectItem = ({item, deleteProject}) => {
    return (
        <tr>
            <td>{item.projectName}</td>
            <td>{item.repositoryLink}</td>
            <td>{item.users}</td>
            <td><button onClick={() => deleteProject(item.url)} type="button">Delete</button></td>
        </tr>
    )
}

const ProjectList = ({items, deleteProject}) => {
    return (
        <div>
        <table>
            <tr>
                <th>Project Name</th>
                <th>Repository Link</th>
                <th>Participating Users</th>
                <th></th>
            </tr>
            {items.map((item) => <ProjectItem item={item} deleteProject={deleteProject}/>)}
        </table>
           <Link to='/projects/create'>Create</Link>
        </div>
    )
}


export default ProjectList;