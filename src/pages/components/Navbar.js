import React, { useContext } from 'react'
import '../Style/Header.css'
import { Outlet, Link } from "react-router-dom";
import Authcontext from "../../context/Authcontext";

export const Navbar = () => {
  const { user, logout } = useContext(Authcontext);

  return (
      <div className="navbar">
        <nav className="navbar navbar-expand-lg navbar-dark bg-light">
          <Link to="/" className="navbar-brand text-dark">
            Dinner Dash
          </Link>


          <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>

          <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <ul className="navbar-nav mr-auto">
              <li className="nav-item">
                <Link className="nav-link text-dark" to="/">Home <span className="sr-only">(current)</span></Link>
              </li>
            </ul>

            { user && <Link className="btn btn-success mr-2" to="/addrestaurant" role="button">Add Restaurant</Link>}
            { user && <Link className="btn btn-success mr-2" to="/admin" role="button">Dashboard</Link>}
            { user && <button className="btn btn-success mr-2" onClick={logout}>Logout</button>}
            { user && <button disabled={true} className="btn mr-2">User</button> }
            { !user && <Link className="btn btn-success mr-2" to="/Login" role="button">Signin</Link>}
            { !user && <Link className="btn btn-success mr-2" to="/registeruser" role="button">Signup</Link>}

            <Link to="/cart">
              <i className="fa fa-shopping-cart pr-3">
            </i>
            </Link>
            <Outlet />

      </div>
    </nav>
</div >
  )
}
