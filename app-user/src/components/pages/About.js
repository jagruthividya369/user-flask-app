import { React } from "react";

const About = () => {
    return (
        <div className="jumbotron jumbotron-fluid border shadow">
            <div className="container1">
                <h1 className="display-4"><center>About the application</center></h1>
                <br></br>
                <hr></hr>
                <br></br>
                <p>This application is created using Flask Framework and MySQL Database.</p>
                In this Web App, User Able to perform following actions.
                <li>Create a New User </li>
                <li>Retrieve details of user searching by
                    <ul>
                        <li>First Name</li>
                        <li>Last Name</li>
                        <li>Phone Number</li>
                    </ul>
                </li>
                <li>Update User Details</li>
                <li>Delete User Details</li>
            </div>
        </div>
    );
};

export default About;