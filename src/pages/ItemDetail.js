import React, {useEffect, useState} from 'react'
import { useParams } from 'react-router';
import {Navbar} from './components/Navbar'
import {Hero} from './components/Hero'
import {useNavigate} from 'react-router-dom';


import axios from "axios";
import './Style/Itemdetail.css'

export const ItemDetail = (props) => {
  const { itemid } = useParams();
  const navigate = useNavigate();

  const [itemdetail, setitemdetail] = useState({
    'title': '',
    'description': '',
    'price': '',
    'available': '',
    'restaurant': ''
  });

  const [baseURL, setbaseURL] = useState("http://localhost:8000/api/getitemdetail/");

  const getitemdetail = async () => {

    try{
          axios.get(`${baseURL}${itemid}`)
          .then((response) => {
            setitemdetail({
              'title': response.data['title'],
              'description': response.data['description'],
              'price': response.data['price'],
              'available': response.data['available'],
              'restaurant': response.data['restaurant'],
              });
            })
            .catch(function (error) {
              navigate('/*');
            });


    } catch (error) {
      console.log("page not found");
    }

    };

    useEffect(() => {
      getitemdetail();
 }, []);

  return (
    <div>
      <Navbar />
      <Hero />

        <div className="detail-container  my-3">
          <div className="left-side" >
              <img className="object-image-1" src="https://res.cloudinary.com/dzag0ldw1/image/upload/v1659178532/gakiweohz9yqelxpbas0.webp" alt="{itemdetail.title}"></img>
          </div>
          <div className='right-side'>
              <h3 className="object-heading my-2">{ itemdetail.title}</h3>
              <p className="object-description ">{ itemdetail.description}</p>

              <div className="object-action">
                <h4 className="object-price-1 mt-2"> PKR { itemdetail.price }</h4>

                {
                itemdetail.available ?
                <button className='object-add-cart-1'> Add to Cart</button>
                : <button disabled={true} className='object-add-cart-1'> Not Available</button>
                }



              </div>
          </div>
        </div>
      {itemid}
      {itemdetail.title}

    </div>
  )
}
