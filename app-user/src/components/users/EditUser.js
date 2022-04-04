import React, { useState, useEffect } from "react"
import axios from "axios"
import { useNavigate, useParams } from "react-router-dom";

const EditUser = () => {
    let navigate = useNavigate();
    const { id } = useParams();
    const [user, setUser] = useState({
        firstname: "",
        lastname: "",
        address: "",
        phone: 0
    });
    const { firstname, lastname, address, phone } = user;
    const onInputChange = e => {
        setUser({ ...user, [e.target.name]: e.target.value });
    };
    useEffect(() => {
        loadUser();
    }, [])

    const onSubmit = async e => {
        e.preventDefault();
        await axios.put("/user", user)
            .then((response) => {
                if (response.status === 200) {
                    alert("User Details Updated");
                    if (window.confirm("Do you still want to edit user details?") === true) {
                        navigate("/user/edit/" + user.id)
                    }
                    else {
                        navigate("/")
                    }
                }
                else {
                    alert("Some Error Occured Please try again")
                    navigate("/user/edit/" + user.id)
                }
            })
            .catch((error) => {
                if (error.response.status === 400) {
                    if (window.confirm(error.response.data.message) !== true) {
                        if (window.confirm("Do you still want to update user details?") === true) {
                            navigate("/user/edit/" + user.id)
                        }
                        else {
                            navigate("/")
                        }
                    }
                }
            });
    };

    const loadUser = async () => {
        const result = await axios.get("/user/id/" + id);
        setUser(result.data)

    }
    return (
        <div className="jumbotron jumbotron-fluid border shadow">
            <div className="container">
                <div className="w-75 mx-auto shadow p-5 m-5">
                    <h2 className="text-center mb-4">Edit the User Details</h2>
                    <form onSubmit={e => onSubmit(e)}>
                        <div className="form-group">
                            <input
                                type="text"
                                className="form-control form-control-lg"
                                placeholder="Enter Your First Name"
                                name="firstname"
                                value={firstname}
                                required
                                minLength="3"
                                maxLength="15"
                                onChange={e => onInputChange(e)}
                            />
                        </div>
                        <br></br>
                        <div className="form-group">
                            <input
                                type="text"
                                className="form-control form-control-lg"
                                placeholder="Enter Your Last Name"
                                name="lastname"
                                value={lastname}
                                required
                                minLength="3"
                                maxLength="15"
                                onChange={e => onInputChange(e)}
                            />
                        </div>
                        <br></br>
                        <div className="form-group">
                            <input
                                type="text"
                                className="form-control form-control-lg"
                                placeholder="Enter Your Address"
                                name="address"
                                value={address}
                                required
                                minLength="3"
                                maxLength="15"
                                onChange={e => onInputChange(e)}
                            />
                        </div>
                        <br></br>
                        <div className="form-group">
                            <input
                                type="number"
                                min="1111111111"
                                max="9999999999"
                                className="form-control form-control-lg"
                                placeholder="Enter Your Phone Number"
                                name="phone"
                                value={phone}
                                required
                                onChange={e => onInputChange(e)}
                            />
                        </div>
                        <br></br>
                        <button className="btn btn-primary btn-block">Update User Details</button>
                    </form>
                </div>
            </div>
        </div>
    );
}

export default EditUser;