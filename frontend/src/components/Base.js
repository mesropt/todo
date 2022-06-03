import React from "react";
import {useLocation} from "react-router-dom";


function PageNotFound404() {
    const url = useLocation();
    return (
        <div>
            <h3>Страница по адресу {`<${url.pathname}>`} не найдена :(</h3>
        </div>
    )
}

export {PageNotFound404};