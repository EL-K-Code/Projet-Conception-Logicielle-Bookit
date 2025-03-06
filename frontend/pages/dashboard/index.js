import { useEffect, useState } from 'react';

// material-ui
import { Grid } from '@mui/material';

// project imports
import EventCard from '@/components/dashboard/EventCard';
import { gridSpacing } from '@/store/constants';
// meta export
export const meta = () => ({
    title: 'Dashboard | Berry - React Material Admin Dashboard Template',
    description:
        'Start your next React project with Berry admin template. It build with Reactjs, Material-UI, Redux, and Hook for faster web development.'
});

// ==============================|| DEFAULT DASHBOARD ||============================== //

const Dashboard = () => {
    const [isLoading, setLoading] = useState(true);
    useEffect(() => {
        setLoading(false);
    }, []);

    return (
        <Grid container spacing={gridSpacing}>
            <Grid item xs={12}>
                <Grid container spacing={gridSpacing}>
                    <Grid item lg={4} md={6} sm={6} xs={12}>
                        <EventCard isLoading={isLoading} />
                    </Grid>
                    <Grid item lg={4} md={6} sm={6} xs={12}>
                        {/* <TotalOrderLineCard isLoading={isLoading} /> */}
                    </Grid>
                    <Grid item lg={4} md={12} sm={12} xs={12}>
                        <Grid container spacing={gridSpacing}>
                            <Grid item sm={6} xs={12} md={6} lg={12}>
                                {/* <TotalIncomeDarkCard isLoading={isLoading} /> */}
                            </Grid>
                            <Grid item sm={6} xs={12} md={6} lg={12}>
                                {/* <TotalIncomeLightCard isLoading={isLoading} /> */}
                            </Grid>
                        </Grid>
                    </Grid>
                </Grid>
            </Grid>


            <Grid item xs={12}>
                <Grid container spacing={gridSpacing}>
                    <Grid item xs={12} md={8}>
                        {/* <TotalGrowthBarCard isLoading={isLoading} /> */}
                    </Grid>
                    <Grid item xs={12} md={4}>
                        {/* <PopularCard isLoading={isLoading} /> */}
                    </Grid>
                </Grid>
            </Grid>

        </Grid>
    );
};

export default Dashboard;
