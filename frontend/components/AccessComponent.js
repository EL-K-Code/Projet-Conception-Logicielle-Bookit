import { useSelector } from 'react-redux';

// Fonction pour vérifier si l'utilisateur fait partie des groupes spécifiés
const isUserInGroups = (userGroups, requiredGroups) => {
  return requiredGroups.some(group => userGroups.includes(group));
};

// Composant conditionnel
const AccessComponent = ({ requiredGroups, children }) => {
  // Récupérer les groupes de l'utilisateur depuis le store Redux
  const userGroups = useSelector(state => state.user.groups);

  // Vérifier si l'utilisateur fait partie des groupes requis
  if (isUserInGroups(userGroups, requiredGroups)) {
    return <>{children}</>; // Afficher le composant si l'utilisateur appartient au groupe
  }

  return null; // Ne rien afficher si l'utilisateur ne fait pas partie des groupes
};

export default AccessComponent;
