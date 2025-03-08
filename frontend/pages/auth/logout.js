import { useRouter } from "next/navigation";
// Dans ton composant de déconnexion
import { logoutUser } from '@/store/actions';
import { useDispatch } from 'react-redux';

export default function LogOut(){
    const router = useRouter();
    const dispatch = useDispatch();
    localStorage.clear()
    dispatch(logoutUser())
    return router.push("/auth/login");

}