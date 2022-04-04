import React from 'react'
import './App.css'
import '../node_modules/bootstrap/dist/css/bootstrap.css'
import Home from './components/pages/Home'
import About from './components/pages/About'
import Navbar from './components/layout/Navbar'
import NotFound from './components/pages/NotFound'
import SearchUser from './components/pages/SearchUser'


import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import AddUser from './components/users/AddUser'
import EditUser from './components/users/EditUser'
import ViewUser from './components/users/ViewUser'


function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Routes>
          <Route exact path='/' element={<Home />} />
          <Route exact path='/about' element={<About />} />
          <Route exact path='/user/add' element={<AddUser />} />
          <Route exact path='/user/edit/:id' element={<EditUser />} />
          <Route exact path='/user/view/:id' element={<ViewUser />} />
          <Route exact path='/user/search' element={<SearchUser />} />
          <Route path='*' element={<NotFound />} />
        </Routes>

      </div>
    </Router>



  );
}

export default App;
