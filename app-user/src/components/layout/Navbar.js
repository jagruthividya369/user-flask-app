import React from 'react';
import { Link, NavLink } from 'react-router-dom';

const Navbar = () => {
    return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-black py-5 ">
            <div className='container'>
                <Link className="navbar-brand" to="/">User Application</Link>
                <div className="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul className="navbar-nav mr-auto">
                        <li className="nav-item">
                            <NavLink className="nav-link" to="/about"><b>About</b></NavLink>
                        </li>
                        <li className="nav-item">
                            <NavLink className="nav-link" to="/"><b>List Of Users</b> </NavLink>
                        </li>
                        <li className="nav-item">
                            <NavLink className="nav-link" to="/user/search"><b>Search For a User</b></NavLink>
                        </li>
                    </ul>
                </div>
                <Link to="/user/add" className='btn btn-light'>Add User</Link>
            </div>
        </nav>
    )}

export default Navbar