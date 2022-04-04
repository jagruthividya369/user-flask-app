import { React, useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
const Home = () => {

    const [users, setUser] = useState([]);

    useEffect(() => {
        loadUsers();
    }, []);

    const loadUsers = async () => {
        const result = await axios.get('/users');
        setUser(result.data.users);

    }

    const deleteUser = async id => {
        await axios.delete(`/user/${id}`)
            .then((response) => {
                if (response.status === 200) {
                    alert(response.data.message);
                    loadUsers();
                }
            })
            .catch((error) => {
                if (error.response.status === 404) {
                    alert(error.response.data.message)
                }
            });
        loadUsers();
    }

    return (
        <div className="jumbotron jumbotron-fluid border shadow">
            <div className="container">
                <div className="py-4">
                    <h1> List of Users</h1>

                    <table className="table border shadow">
                        <thead className="thead-dark">
                            <tr>
                                <th scope="col">#</th>
                                <th scope="col">First Name</th>
                                <th scope="col">Last Name</th>
                                <th scope="col">Phone Number</th>
                                <th scope="col">Address</th>
                                <th scope="col">Created On</th>
                                <th scope="col">Updated On</th>
                                <th scope="col">Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            {
                                users.map((user, index) => (
                                    <tr>
                                        <th scope="row">{index + 1}</th>
                                        <td>{user.firstname}</td>
                                        <td>{user.lastname}</td>
                                        <td>{user.phone}</td>
                                        <td>{user.address}</td>
                                        <td>{user.creation_date}</td>
                                        <td>{user.updation_date}</td>
                                        <td>
                                            <Link to={`/user/view/${user.id}`} className="btn btn-outline-success mr-2">View</Link>
                                            <Link to={`/user/edit/${user.id}`} className="btn btn-outline-primary mr-2">Edit</Link>
                                            <Link to="/" className="btn btn-outline-danger" onClick={() => deleteUser(user.id)}>Delete</Link>
                                        </td>
                                    </tr>
                                ))}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    );
};

export default Home;