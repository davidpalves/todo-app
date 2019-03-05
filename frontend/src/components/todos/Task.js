import React from 'react';

const Task = ({ title, description, deadline, status, responsible }) => (
    <li>
        <h3>{title}</h3> {" "}
        <small>
            {description} <br />
            {deadline}<br />
            {String(status)}<br />
            {responsible}<br />
        </small>
    </li>
)

export default Task