"use client";

// material-ui
import { Divider, List, Typography } from '@mui/material';
import { useTheme } from '@mui/material/styles';

// project imports
import AccessComponent from '@/components/AccessComponent';
import NavCollapse from '../NavCollapse';
import NavItem from '../NavItem';

// types
import PropTypes from 'prop-types';

// ==============================|| SIDEBAR MENU LIST GROUP ||============================== //

const NavGroup = ({ item }) => {
    const theme = useTheme();

    // menu list collapse & items
    const parent = item ;
    console.log(parent?.accessGroups);
    const items = item.children?.map((menu) => {
        switch (menu.type) {
            case 'collapse':
                return <NavCollapse key={menu.id} menu={menu} level={1} />;
            case 'item':
                return <NavItem key={menu.id} item={menu} level={1} />;
            default:
                return (
                    <Typography key={menu.id} variant="h6" color="error" align="center">
                        Menu Items Error
                    </Typography>
                );
        }
    });

    return (
        <> <AccessComponent requiredGroups={parent?.accessGroups}>
            <List
                subheader={
                    item.title && (
                        <Typography variant="caption" sx={{ ...theme.typography.menuCaption }} display="block" gutterBottom>
                            {item.title}
                            {item.caption && (
                                <Typography variant="caption" sx={{ ...theme.typography.subMenuCaption }} display="block" gutterBottom>
                                    {item.caption}
                                </Typography>
                            )}
                        </Typography>
                    )
                }
            >
                {items}
            </List>
         </AccessComponent>

            {/* group divider */}
            <Divider sx={{ mt: 0.25, mb: 1.25 }} />
        </>
    );
};

NavGroup.propTypes = {
    item: PropTypes.object
};

export default NavGroup;
