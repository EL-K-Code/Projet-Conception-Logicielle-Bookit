"use client";
import { Link } from 'next/link';
import { useDispatch, useSelector } from 'react-redux';

// material-ui
import { ButtonBase } from '@mui/material';

// project imports
import config from '@/config';
import { MENU_OPEN } from '@/store/actions';
import Logo from '@/ui-component/Logo';

// ==============================|| MAIN LOGO ||============================== //

const LogoSection = () => {
    const defaultId = useSelector((state) => state.customization.defaultId);
    const dispatch = useDispatch();
    return (
        <ButtonBase disableRipple onClick={() => dispatch({ type: MENU_OPEN, id: defaultId })} component={Link} href={config.defaultPath}>
            <Logo />
        </ButtonBase>
    );
};

export default LogoSection;
