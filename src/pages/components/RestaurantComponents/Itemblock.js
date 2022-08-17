import React from 'react'
import { Outlet, Link } from "react-router-dom";

export const Itemblock = (props) => {
  const detailurl = `/item/${props.item.id}`;

  return (
    <div className="object">
      <img className="object-image" src="https://res.cloudinary.com/dzag0ldw1/image/upload/v1659178532/gakiweohz9yqelxpbas0.webp" alt="" />
      <Link to={detailurl}><h3 className="object-heading"> {props.item.title} </h3></Link>

      <p className="object-description">{props.item.description}</p>

      <div className="object-action">
          <p className="object-price"> PKR {props.item.price}</p>

          {
            props.item.available ?
            <button className='object-add-cart'> Add to Cart</button>
            : <button disabled={true} className='object-add-cart'> Not Available</button>
          }

          {/* <button type="button"
                  className="object-add-cart btn UpdateCart">ADD TO CART
          </button> */}
      </div>
      <Outlet/>

    </div>
  )
}

// {props.item.id}
// {props.item.title}
// {props.item.description}
// {props.item.price}
// {props.item.order_count}
