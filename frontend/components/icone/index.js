//lucide-react import
import {
  Activity, Bus, CalendarCheck, CalendarPlus, Edit,
  MoreVertical, Package, School, Trash
} from 'lucide-react';


//Get icone By type
const getIconeByType = (type, theme, handleClick=null) => {
  const iconProps = {
      style: { marginRight: 8 },
      size: 24,
      color: theme.palette.primary.main,
      cursor: handleClick ? 'pointer' : 'default',
      transition: 'transform 0.2s ease, color 0.2s ease',
      onClick : handleClick ? handleClick : undefined
  };

  switch (type) {
      case "room":
          return <School {...iconProps} />;
      case "bus":
          return <Bus {...iconProps} />;
      case "material":
          return <Package {...iconProps} />;
      case "dashboard":
          return <Activity {...iconProps} />;
      case "cancel":
        return <Trash {...iconProps} color={theme.palette.error.main}/>;
      case "calender":
        return <CalendarPlus {...iconProps} />;
      case "edit":
        return <Edit {...iconProps} />;
      case "more":
        return <MoreVertical {...iconProps} color={theme.palette.common.white}/>;
      case "date":
        return <CalendarCheck {...iconProps}/>
      default:
          return null;
  }
};


export default getIconeByType ;