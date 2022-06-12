import React from 'react'
import {Link} from "react-router-dom";

const Menu = () => {
    return (
        <div class="container-fluid">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li className="nav-item"><Link class="nav-link" to='/mainpage'>Main Page</Link></li>
                <li class="nav-item"><Link class="nav-link" to='/projects'>Projects</Link></li>
                <li className="nav-item"><Link class="nav-link" to='/users'>Users</Link></li>
                <li class="nav-item"><Link class="nav-link" to='/todos'>ToDos</Link></li>
            </ul>
        </div>
    );
};

export default Menu;