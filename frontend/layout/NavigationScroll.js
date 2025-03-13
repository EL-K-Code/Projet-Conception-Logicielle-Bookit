"use client";

import { useRouter } from "next/router"; // Pour Next.js avec pages directory
import PropTypes from "prop-types";
import { useEffect } from "react";

// ==============================|| NAVIGATION SCROLL TO TOP ||============================== //

const NavigationScroll = ({ children }) => {
    const router = useRouter();

    useEffect(() => {
        const handleRouteChange = () => {
            window.scrollTo({
                top: 0,
                left: 0,
                behavior: "smooth",
            });
        };

        router.events.on("routeChangeComplete", handleRouteChange);
        return () => {
            router.events.off("routeChangeComplete", handleRouteChange);
        };
    }, [router]);

    return <>{children}</>;
};

NavigationScroll.propTypes = {
    children: PropTypes.node,
};

export default NavigationScroll;
