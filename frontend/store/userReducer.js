// userReducer

"use client"

import { LOGOUT_USER, SET_USER_GROUP } from "@/store/actions";

const initialState = {
  groups: typeof window !== 'undefined' && localStorage.getItem('userGroups')
    ? JSON.parse(localStorage.getItem('userGroups'))
    : ['anonymous'],
};

const userReducer = (state = initialState , action) => {
    switch (action.type) {
      case SET_USER_GROUP:
        localStorage.setItem('userGroups', JSON.stringify(action.payload));
        return {
          ...state,
          groups: action.payload,  // Met à jour les groupes avec les données reçues (après connexion)
        };
      case LOGOUT_USER :
        return {
          ...state,
          groups: ['anonymous'],  // Réinitialise les groupes à 'anonymous' lors de la déconnexion
        };
      default:
        return state;
    }
  };



export default userReducer;
