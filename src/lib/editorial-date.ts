const bangkokDate = new Intl.DateTimeFormat("sv-SE", {
  timeZone: "Asia/Bangkok",
  year: "numeric",
  month: "2-digit",
  day: "2-digit",
});

export function formatEditorialDate(date: Date): string {
  return bangkokDate.format(date);
}
