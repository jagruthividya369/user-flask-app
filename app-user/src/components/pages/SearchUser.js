import React, { useState } from "react"
import axios from "axios"
import { Link } from "react-router-dom";

const SearchUser = () => {

    const [fname, setFirstName] = useState([]);
    const [lname, setLastName] = useState([]);
    const [phno, setPhNo] = useState([]);
    const [result, setResultState] = useState([]);

    const onSubmitFirstName = async e => {
        e.preventDefault();
        await axios.get("/user/firstname/" + fname['firstname'])
            .then((response) => {
                setResultState(response.data.users)
            })
            .catch((error) => {
                if (error.response.status === 404) {
                    alert("No Such User Found")
                    setResultState([])
                }
            });

    };
    const onSubmitLastName = async e => {
        e.preventDefault();
        await axios.get("/user/lastname/" + lname['lastname'])
            .then((response) => {
                setResultState(response.data.users)
            })
            .catch((error) => {
                if (error.response.status === 404) {
                    alert("No Such User Found")
                    setResultState([])
                }
            });
    };

    const searchFirstAndLastName = async e => {
        await axios.get("/user/firstlastname/" + fname['firstname'] + "," + lname['lastname'])
        .then((response) => {
            setResultState(response.data.users)
        })
            .catch((error) => {
                if (error.response.status === 404) {
                    alert("No Such User Found")
                    setResultState([])
                }
            });
    };

    const onSubmitPhone = async e => {
        e.preventDefault();
        await axios.get("/user/phone/" + phno['phone'])
            .then((response) => {
                setResultState(response.data.users)
            })
            .catch((error) => {
                if (error.response.status === 404) {
                    alert("No Such User Found")
                    setResultState([])
                }
            });
    };

    const onInputChange = e => {
        setFirstName({ ...fname, [e.target.name]: e.target.value });
        setLastName({ ...lname, [e.target.name]: e.target.value });
        setPhNo({ ...phno, [e.target.name]: e.target.value })
    };

    return (
        <div className="jumbotron jumbotron-fluid border shadow">
            <div className="container">
                <div className="py-4">
                    <h1> User Search</h1>
                    <form onSubmit={fname => onSubmitFirstName(fname)}>
                        <div className="form-group">
                            <input
                                type="search"
                                name="firstname"
                                placeholder="Search By First Name"
                                className="form-control"
                                onChange={e => onInputChange(e)}
                            />
                            <br></br>
                            <button type="submit" className="btn btn-success">Search By First Name</button>
                        </div>
                    </form>
                    <br></br>
                    <form onSubmit={lname => onSubmitLastName(lname)}>
                        <div className="form-group">
                            <input
                                type="search"
                                name="lastname"
                                placeholder="Search By Last Name"
                                className="form-control"
                                onChange={e => onInputChange(e)}
                            />
                            <br></br>
                            <button type="submit" className="btn btn-success">Search By Last Name</button>
                        </div>
                    </form>
                    <br></br>
                    <button onClick={() => searchFirstAndLastName(fname, lname)} className="btn btn-success">Search By First and Last Name</button>
                    <br></br>
                    <form onSubmit={phno => onSubmitPhone(phno)}>
                        <br></br>
                        <div className="form-group">
                            <input
                                type="number"
                                name="phone"
                                min="1111111111"
                                max="9999999999"
                                placeholder="Search By Phone Number"
                                className="form-control"
                                onChange={e => onInputChange(e)}
                            />
                            <br></br>
                            <button type="submit" className="btn btn-success">Search By Phone Number</button>
                        </div>
                    </form>

                </div>
                <div className="output">
                    <div className="container">
                        <div className="py-4">
                            <h1>Results</h1>
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
                                        result.map((user, index) => (
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
                                                </td>
                                            </tr>
                                        ))
                                    }
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};
export default SearchUser;