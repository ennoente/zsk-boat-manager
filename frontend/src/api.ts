//const BACKEND_HOST = "backend";

type TIsBoatCheckedInResponse = {
  isBoatCheckedIn: boolean
}

export const isBoatAlreadyCheckedIn = async (boatName: string): Promise<boolean> => {
  const response = await fetch(`/api/is-boat-checked-in?boatname=${boatName}`);
  const result = await response.json();

  return result.isBoatCheckedIn;
}
