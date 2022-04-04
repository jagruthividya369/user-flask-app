import React, { useState, useEffect } from "react"
import axios from "axios"
import { Link } from "react-router-dom";

import { useParams } from "react-router-dom";

const ViewUser = () => {
    const [user, setUser] = useState({
        firstname: "",
        lastname: "",
        address: "",
        phone: 0,
        creation_date: "",
        updation_date: ""
    });
    const { id } = useParams();

    useEffect(() => {
        loadUser();
    }, [])

    const loadUser = async () => {
        const result = await axios.get("/user/id/" + id);
        setUser(result.data)

    }
    return (
        <div className="jumbotron jumbotron-fluid border shadow">
            <div className="container py-4">
                <h1>User Details</h1>
                <hr />
                <ul className="list-group shadow border p-5 m-5" >
                    <li className="list-group-item"><b>User Id:</b> {user.id}</li>
                    <li className="list-group-item"><b>First Name:</b> {user.firstname}</li>
                    <li className="list-group-item"><b>Last Name:</b> {user.lastname}</li>
                    <li className="list-group-item"><b>Phone Number:</b> {user.phone}</li>
                    <li className="list-group-item"><b>Address:</b> {user.address}</li>
                    <li className="list-group-item"><b>User Created On:</b> {user.creation_date}</li>
                    <li className="list-group-item"><b>User Updated On:</b> {user.updation_date}</li>
                </ul>
                <Link to='/' className="btn btn-outline-success">Back to Home </Link>
            </div>
        </div>
    )

}

export default ViewUser;