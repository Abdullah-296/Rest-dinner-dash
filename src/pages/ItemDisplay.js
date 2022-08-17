import React, {useEffect, useState} from 'react'
import { useParams } from 'react-router';
import {Navbar} from './components/Navbar'
import {Hero} from './components/Hero'
import { Itemblock } from './components/RestaurantComponents/Itemblock';
import axios from "axios";


export const ItemDisplay = (props) => {
  const { restaurantid } = useParams();

  const [Restaurantitems, setRestaurantitems] = useState({
    'Name': 'Restaurant',
    'Address': 'Islamabad',
    'items': [],
  });

  const [baseURL, setbaseURL] = useState("http://localhost:8000/api/getrestaurantdetail/");

  const getrestaurantitemdata = () => {
    axios.get(`${baseURL}${restaurantid}`)
    .then((response) => {
      setRestaurantitems({
         'Name': response.data['Name'],
         'Address': response.data['Address'],
         'items': response.data['items'],
         });
      })
    };

    useEffect(() => {
      getrestaurantitemdata();
 }, [baseURL]);


  return (
    <div>
      <Navbar />
      <Hero />


      <div className="category-heading my-3 py-3">
        <h2>{Restaurantitems.Name}</h2>
      </div>
      <div className='item-main-container'>
      {Restaurantitems.items.map((item) =>
            <Itemblock key={item.id} item={item} />
            )}

      </div>

    </div>

  )
}

// ItemDisplay
//       {restaurantid}
//       <p> {`${baseURL}${restaurantid}`}</p>

//       {Restaurantitems.Name}
//       {Restaurantitems.Address}
