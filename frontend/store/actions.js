// action - customization reducer
export const SET_MENU = '@customization/SET_MENU';
export const MENU_TOGGLE = '@customization/MENU_TOGGLE';
export const MENU_OPEN = '@customization/MENU_OPEN';
export const SET_FONT_FAMILY = '@customization/SET_FONT_FAMILY';
export const SET_BORDER_RADIUS = '@customization/SET_BORDER_RADIUS';

//user action reducer
export const SET_USER_GROUP = '@user/SET_USER_GROUP';
export const LOGOUT_USER = '@user/LOGOUT_USER';


export const setUserGroup = (groups) => ({
  type: SET_USER_GROUP,
  payload: groups,  // Met à jour les groupes récupérés après la connexion
});

export const logoutUser = () => ({
    type: LOGOUT_USER,  // Réinitialise les groupes lors de la déconnexion
  });
