import React from 'react'
import '../../Style/Restaurant.css'
import { Outlet, Link } from "react-router-dom";


export const Restaurantblock = (props) => {

  const detailurl = `/restaurant/${props.restaurant.id}`;

  return (
    <div className='object'>
      <img className="object-image" src="https://res.cloudinary.com/dzag0ldw1/image/upload/v1659178532/gakiweohz9yqelxpbas0.webp" alt={props.restaurant.Name}></img>

      <Link to={detailurl}><h3 className="object-heading">{props.restaurant.Name}</h3></Link>


      <p className="object-description">
        {props.restaurant.description}
        <br></br>
        <i className="fa fa-map-marker" aria-hidden="true"></i>
        {props.restaurant.Address}
      </p>
      <Outlet />


    </div>
  )
}


// {props.restaurant.id}
//       {props.restaurant.id}
//       {props.restaurant.Name}
//       {props.restaurant.Address}
//       {props.restaurant.description}
//       {props.restaurant.photo}
