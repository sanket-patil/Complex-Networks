function ipi = assign(ipi,y,varargin)
% IPINT32/ASSIGN Assign an entire in-place int32.
%
% assign(ipi,y) overwrites the contents of ipi with y.  The size of ipd and
% y must match.
%
% Example:
%    ipi = ipint32(int32(ones(5,1)));
%    assign(ipi,int32(3*ones(5,1)));

if (isempty(x))

    if any(size(size(ipi)) ~= size(size(y))) || ...
       any(size(ipi) ~= size(y))
        error('ipdouble:invalidParameter','In assign(ipd,y) size(ipd) must equal size(y).');
    end;

    subs = {':'};
    S = struct('type','()','subs',[]);
    S.subs = subs;
    subsasgn(ipi,S,y);
else
    S = struct('type','()','subs',[]);
    S.subs = varargin;
    subsasgn(ipi,S,y);
end;