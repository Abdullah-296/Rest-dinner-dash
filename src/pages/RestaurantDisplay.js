import React from 'react'
import {Navbar} from './components/Navbar'
import {Hero} from './components/Hero'
import { Restaurants } from './components/RestaurantComponents/Restaurants'

export const RestaurantDisplay = () => {
  return (
    <div>

      <Navbar />
      <Hero />
      <Restaurants />

    </div>
  )
}
